# Generated by Django 5.0.1 on 2024-02-02 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core1', '0003_package_remove_packages1_exterior_package_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='types',
            field=models.CharField(choices=[('interior', 'Interior'), ('exterior', 'Exterior'), ('extra', 'Extra')], db_index=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='package',
            name='level',
            field=models.CharField(choices=[('level_one', 'Level One'), ('level_two', 'Level Two'), ('level_three', 'Level Three')], db_index=True, default='', max_length=20),
        ),
    ]
