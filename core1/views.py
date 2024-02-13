from django.http import HttpResponse
from core1.models import Levels
from django.shortcuts import render
from django.http import JsonResponse
# import requests
import requests
# For read json
import json
# Generating tokkens
import uuid

def engine(request):
    if request.method == "POST":
        try:
            # Creating a random token id
            token_id = uuid.uuid4()
    
            # Getting template data
            reg = request.POST.get('reg')  # Use POST instead of GET for form data
            
            # Retrieving data from the external API
            try:
                url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"
                data = {"registrationNumber": reg}
                headers = {'x-api-key': '7TUL5z8I1t4M12xIxDJVE9wkQjDB4tB5RlnlYGk5',
                           'Content-Type': 'application/json'}
                response = requests.post(url, headers=headers, data=json.dumps(data))
                response.raise_for_status()  # Raise HTTPError for bad responses
            except requests.RequestException as e:
                # Handle request exceptions
                return JsonResponse({'error': str(e)}, status=500)
            
            # Convert response to JSON
            car_info = response.json()

            # Check if the car with the given registration number already exists
            engine = int(car_info.get('engineCapacity', ''))  # Convert engine to int
            
            # Retrieve the level based on the engine capacity
            level = Levels.get_level(engine)
      
            if level:
                # Retrieve packages associated with the level
                packages = level.packages.all()
                # Prepare context for rendering the template
                context = {
                    "engine": engine,
                    "level": level,
                    "packages": packages,
                }

                # Render the template with the context
                return render(request, 'core1/cuspack.html', context)
            else:
                # Return a response indicating that the engine value is not in the expected range
                return JsonResponse({'error': 'Engine value is not in the expected range'}, status=400)

        except Exception as e:
            # Handle other exceptions
            error_message = str(e)
            print(error_message)
            return JsonResponse({'error': error_message}, status=500)
    else:
        return HttpResponse("This method is not allowed")



def packages(request):

    return render(request, "core1/packages.html")
