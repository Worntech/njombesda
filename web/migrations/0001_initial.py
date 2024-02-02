# Generated by Django 4.2.3 on 2024-01-31 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=100, null=True)),
                ('Subject', models.CharField(max_length=100, null=True)),
                ('Email', models.EmailField(max_length=200, null=True)),
                ('Phone', models.CharField(max_length=100, null=True)),
                ('Message', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mafundisho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=700)),
                ('Explanation', models.CharField(max_length=500)),
                ('Image', models.ImageField(upload_to='home/')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Matangazo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=700)),
                ('Explanation', models.CharField(max_length=500)),
                ('Image', models.ImageField(upload_to='home/')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Matukio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=700)),
                ('Explanation', models.CharField(max_length=500)),
                ('Image', models.ImageField(upload_to='home/')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='email')),
                ('first_name', models.CharField(max_length=100, verbose_name='first name')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='username')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('hide_email', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=700)),
                ('Course', models.CharField(choices=[('Frontend', 'Frontend'), ('Backend', 'Backend'), ('Fullstack', 'Fullstack')], max_length=200, null=True)),
                ('Part', models.CharField(choices=[('html and css', 'html and css'), ('javascript', 'javascript'), ('React js', 'React js'), ('Vue js', 'Vue js'), ('Bootstrap', 'Bootstrap'), ('Angular js', 'Angular js'), ('Django', 'Django'), ('Flask', 'Flask'), ('Php', 'Php'), ('Laravel', 'Laravel'), ('Rub', 'Rub'), ('Django, html and css', 'Django, html and css'), ('Flask, html and css', 'Flask, html and css'), ('Django and react js', 'Django and react js'), ('Php, html and css', 'Php, html and css'), ('Php and react js', 'Php and react js'), ('Laravel, html and css', 'Laravel, html and css')], max_length=200, null=True)),
                ('Explanation', models.CharField(max_length=500)),
                ('Image', models.ImageField(upload_to='home/')),
                ('Video', models.FileField(upload_to='home/')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Washiriki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Jina_La_Kwanza', models.CharField(max_length=100)),
                ('Jina_La_Pili', models.CharField(max_length=100)),
                ('Jina_La_Mwisho', models.CharField(max_length=100)),
                ('Mahali_Anapoishi', models.CharField(max_length=100)),
                ('Namba_Ya_Simu', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='home/')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.myuser')),
            ],
        ),
        migrations.CreateModel(
            name='Commentwebsite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.website')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Commentmatukio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.matangazo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Commentmatangazo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.matangazo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Commentmafundisho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.mafundisho')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
