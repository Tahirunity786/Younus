# Generated by Django 5.0.1 on 2024-02-01 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Packages_1_extra_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(db_index=True, default='', max_length=100)),
                ('price', models.IntegerField(db_index=True, default=0)),
                ('package_description', models.TextField(db_index=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Packages_2_extra_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(db_index=True, default='', max_length=100)),
                ('price', models.IntegerField(db_index=True, default=0)),
                ('package_description', models.TextField(db_index=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Packages_3_extra_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(db_index=True, default='', max_length=100)),
                ('price', models.IntegerField(db_index=True, default=0)),
                ('package_description', models.TextField(db_index=True, default='')),
            ],
        ),
        migrations.AddField(
            model_name='packages1',
            name='extra_package',
            field=models.ManyToManyField(related_name='level_one_extra_package', to='core1.packages_1_extra_data'),
        ),
        migrations.AddField(
            model_name='packages2',
            name='extra_package',
            field=models.ManyToManyField(related_name='level_two_extra_package', to='core1.packages_2_extra_data'),
        ),
        migrations.AddField(
            model_name='packages3',
            name='extra_package',
            field=models.ManyToManyField(related_name='level_three_extra_package', to='core1.packages_3_extra_data'),
        ),
    ]
