# Generated by Django 3.2.4 on 2021-06-25 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0006_mymodel_datetime_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='o_field',
            field=models.Field(null=True),
        ),
    ]
