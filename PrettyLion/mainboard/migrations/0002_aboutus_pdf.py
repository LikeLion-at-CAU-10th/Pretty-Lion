# Generated by Django 4.0.1 on 2022-03-14 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='aboutus/'),
        ),
    ]
