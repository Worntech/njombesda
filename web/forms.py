from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class MyUserForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['email', 'username', 'first_name']
        
# class WashirikiForm(ModelForm):
#     class Meta:
#         model = Washiriki
#         fields = '__all__'


    #for contact 
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
     
     #for website
class WebsiteForm(ModelForm):
    class Meta:
        model = Website
        fields = '__all__'


# for church website
class MafundishoForm(ModelForm):
    class Meta:
        model = Mafundisho
        fields = '__all__'
        
class CommentmafundishoForm(ModelForm):
    class Meta:
        model = Commentmafundisho
        fields = '__all__'
        
class MatangazoForm(ModelForm):
    class Meta:
        model = Matangazo
        fields = '__all__'
        
class CommentmatangazoForm(ModelForm):
    class Meta:
        model = Commentmatangazo
        fields = '__all__'
        
class WashirikiForm(ModelForm):
    class Meta:
        model = Washiriki
        fields = '__all__'
        
class MatukioForm(ModelForm):
    class Meta:
        model = Matukio
        fields = '__all__'
        
class CommentmatukioForm(ModelForm):
    class Meta:
        model = Commentmatukio
        fields = '__all__'
   