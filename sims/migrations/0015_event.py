# Generated by Django 4.2.3 on 2023-12-20 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sims', '0014_studentcontactinfo_profile_image_staffcontactinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event_Name', models.CharField(max_length=100)),
                ('Event_Place', models.CharField(max_length=100)),
                ('Event_Start', models.CharField(max_length=100)),
                ('Event_End', models.CharField(max_length=100)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
            ],
        ),
    ]
