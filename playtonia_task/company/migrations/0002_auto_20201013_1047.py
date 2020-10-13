# Generated by Django 3.1.2 on 2020-10-13 10:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='employees',
        ),
        migrations.AlterField(
            model_name='company',
            name='contact_no',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message="contact number must be entered in the format: '9999999999'. Up to 10 digits allowed.", regex='^\\+?1?\\d{10,10}$')]),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]