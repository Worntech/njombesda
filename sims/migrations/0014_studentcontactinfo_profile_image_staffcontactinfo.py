# Generated by Django 4.2.3 on 2023-12-19 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sims', '0013_finalresult_academic_year_finalresult_semister_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentcontactinfo',
            name='Profile_Image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='home/'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='StaffContactinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_type', models.CharField(choices=[('Staff', 'Staff')], max_length=40)),
                ('First_Name', models.CharField(max_length=100)),
                ('Middle_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Collage', models.CharField(choices=[('coste', 'coste'), ('coict', 'coict')], max_length=40)),
                ('Department', models.CharField(choices=[('computer engineering', 'computer engineering'), ('computer science', 'computer science'), ('civil engineering', 'civil engineering')], max_length=40)),
                ('Level_Of_Education', models.CharField(choices=[('Certificate', 'Certificate'), ('Diploma', 'Diploma'), ('Bachelor', 'Bachelor'), ('Master', 'Master'), ('Phd', 'Phd')], max_length=40)),
                ('course', models.CharField(choices=[('Computer Engineering', 'Computer Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Mechanical Engineering', 'Mechanical Engineering')], max_length=40)),
                ('Region', models.CharField(choices=[('Arusha', 'Arusha'), ('Dodoma', 'Dodoma'), ('Mwanza', 'Mwanza'), ('Iringa', 'Iringa'), ('Tabora', 'Tabora')], max_length=40)),
                ('Phone', models.CharField(max_length=100)),
                ('Form4_Certificate', models.FileField(upload_to='home/')),
                ('Form6_Certificate', models.FileField(upload_to='home/')),
                ('Univercity_Certificate', models.FileField(upload_to='home/')),
                ('Profile_Image', models.ImageField(upload_to='home/')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
