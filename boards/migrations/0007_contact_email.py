# Generated by Django 3.1 on 2021-10-08 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0006_contact_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
