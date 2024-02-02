from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.contrib import messages


# user table--------------------------------------------------------------------
class MyUserManager(BaseUserManager):
    def create_user(self, email, username, first_name, password=None):
        if not email:
            raise ValueError("email is required")
        if not username:
            raise ValueError("Your user name is required")
        if not first_name:
            raise ValueError("Your First Name is required")
        # if not last_name:
        #     raise ValueError("Your Last Name is required")
        # if not id:
        #     raise ValueError("Your Middle Name is required")
        
        

        user=self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            # last_name=last_name,
            # middle_name=middle_name,
            # phone=phone,
            # id=id,
            # course=course,
            
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            # first_name=first_name,
            # last_name=last_name,

        )
        user.is_admin=True
        user.is_staff=True
        
        user.is_superuser=True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email=models.EmailField(verbose_name="email", max_length=100, unique=True)
    first_name=models.CharField(verbose_name="first name", max_length=100, unique=False)
    username=models.CharField(verbose_name="username", max_length=100, unique=True)
    # id=models.CharField(verbose_name="id", max_length=100, unique=False, primary_key=True)
    # last_name=models.CharField(verbose_name="last name", max_length=100, unique=False)
    
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    
    last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)
    


    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['username']
    
    objects=MyUserManager()

    def __str__(self):
        return self.username

    


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
class Washiriki(models.Model):
    Years = [
    ("2024", "2024"),
    ("2025", "2025"),
    ("2026", "2026"),
    ("2027", "2027"),
    ("2028", "2028"),
]
    aina = [
    ("Mshiriki", "Mshiriki"),
    ("mzee wa kanisa", "mzee wa kanisa"),
    ("karani", "karani"),
    ("shemasi mkuu wa kiume", "shemasi mkuu wa kiume"),
    ("shemasi mkuu wa kike", "shemasi mkuu wa kike"),
]
    Namba_ya_Ushirika = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    Jina_La_Kwanza = models.CharField(max_length=100)
    Jina_La_Pili = models.CharField(max_length=100)
    Jina_La_Mwisho = models.CharField(max_length=100)
    Mahali_Anapoishi = models.CharField(max_length=100)
    Aina = models.CharField(max_length=40, choices=aina)
    Namba_Ya_Simu = models.CharField(max_length=100)
    Image =models.ImageField(upload_to="home/")
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    
# class StudentContactinfo(models.Model):
#     region = [
#     ("Arusha", "Arusha"),
#     ("Dodoma", "Dodoma"),
#     ("Mwanza", "Mwanza"),
#     ("Iringa", "Iringa"),
#     ("Tabora", "Tabora"),
# ]
#     user_type = [
#     ("Student", "Student"),
# ]
#     Course = [
#     ("Computer Engineering", "Computer Engineering"),
#     ("Electrical Engineering", "Electrical Engineering"),
#     ("Mechanical Engineering", "Mechanical Engineering"),
# ]
#     level = [
#     ("Certificate", "Certificate"),
#     ("Diploma", "Diploma"),
#     ("Bachelor", "Bachelor"),
#     ("Master", "Master"),
#     ("Phd", "Phd"),
# ]
#     Years = [
#     ("1", "1"),
#     ("2", "2"),
#     ("3", "3"),
#     ("4", "4"),
#     ("5", "5"),
# ]
#     collage = [
#     ("coste", "coste"),
#     ("coict", "coict"),
# ]
#     department = [
#     ("computer engineering", "computer engineering"),
#     ("computer science", "computer science"),
#     ("civil engineering", "civil engineering"),
# ]
#     user = models.ForeignKey(MyStaff, on_delete=models.CASCADE)
#     User_type = models.CharField(max_length=40, choices=user_type)
#     First_Name = models.CharField(max_length=100)
#     Middle_Name = models.CharField(max_length=100)
#     Last_Name = models.CharField(max_length=100)
#     Collage = models.CharField(max_length=40, choices=collage)
#     Department = models.CharField(max_length=40, choices=department)
#     Level = models.CharField(max_length=40, choices=level)
#     course = models.CharField(max_length=40, choices=Course)
#     years = models.CharField(max_length=40, choices=Years)
#     Region = models.CharField(max_length=40, choices=region)
#     Phone = models.CharField(max_length=100)
#     Profile_Image =models.ImageField(upload_to="home/")
#     date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)


# end user table -------------
# Create your models here.
class Contact(models.Model):
    Full_Name = models.CharField(max_length=100, null=True)
    Subject = models.CharField(max_length=100, null=True)
    Email = models.EmailField(max_length=200, null=True)
    Phone = models.CharField(max_length=100, null=True)
    Message = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


# for the courses to be uploaded
class Website(models.Model):
    courses = (
            ('Frontend', 'Frontend'),
			('Backend', 'Backend'),
			('Fullstack', 'Fullstack'),
			)
    part = (
            ('html and css', 'html and css'),
			('javascript', 'javascript'),
			('React js', 'React js'),
            ('Vue js', 'Vue js'),
			('Bootstrap', 'Bootstrap'),
			('Angular js', 'Angular js'),
            ('Django', 'Django'),
			('Flask', 'Flask'),
			('Php', 'Php'),
            ('Laravel', 'Laravel'),
			('Rub', 'Rub'),
			('Django, html and css', 'Django, html and css'),
            ('Flask, html and css', 'Flask, html and css'),
			('Django and react js', 'Django and react js'),
			('Php, html and css', 'Php, html and css'),
            ('Php and react js', 'Php and react js'),
			('Laravel, html and css', 'Laravel, html and css'),
			)
    Title = models.CharField(max_length=700)
    Course = models.CharField(max_length=200, null=True, choices=courses)
    Part = models.CharField(max_length=200, null=True, choices=part)
    Explanation = models.CharField(max_length=500)
    Image =models.ImageField(upload_to="home/")
    Video = models.FileField(upload_to="home/")
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
class Commentwebsite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Website', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.Full_Name
    
    
# models for church
class Mafundisho(models.Model):
    Title = models.CharField(max_length=700)
    Explanation = models.CharField(max_length=500)
    Image =models.ImageField(upload_to="home/")
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
class Commentmafundisho(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Mafundisho', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.username
    
class Matangazo(models.Model):
    Title = models.CharField(max_length=700)
    Explanation = models.CharField(max_length=500)
    Image =models.ImageField(upload_to="home/")
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
class Commentmatangazo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Matangazo', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.username
    
# class Washiriki(models.Model):
#     aina = (
#             ('Mshiriki', 'Mshiriki'),
# 			('Muumini wa shule ya sabato', 'Muumini wa shule ya sabato'),
# 			('Darasa la ubatizo', 'Darasa la ubatizo'),
# 			)
#     Jina_Kamili = models.CharField(max_length=700)
#     Mahali_Anapoishi = models.CharField(max_length=700)
#     Uhusika = models.CharField(max_length=200, null=True, choices=aina)
#     Image =models.ImageField(upload_to="home/")
#     date_created = models.DateTimeField(auto_now_add=True, null=True)
    
class Matukio(models.Model):
    Title = models.CharField(max_length=700)
    Explanation = models.CharField(max_length=500)
    Image =models.ImageField(upload_to="home/")
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
class Commentmatukio(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Matangazo', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.username
    
