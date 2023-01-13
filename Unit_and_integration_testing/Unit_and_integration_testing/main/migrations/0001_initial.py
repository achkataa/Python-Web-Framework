# Generated by Django 4.0.4 on 2022-04-18 05:57

import Unit_and_integration_testing.main.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, validators=[Unit_and_integration_testing.main.validators.only_letters_validator])),
                ('last_name', models.CharField(max_length=30, validators=[Unit_and_integration_testing.main.validators.only_letters_validator])),
                ('age', models.IntegerField()),
            ],
        ),
    ]
