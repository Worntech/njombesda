from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User, auth
from . models import *
from . forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView

from django.conf import settings

# from web.views import *

from django.shortcuts import render, get_object_or_404
from django.http import Http404

from django.contrib.auth import get_user_model

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from django.db.models import Sum
from django.shortcuts import get_list_or_404

# Create your views here.
# @login_required(login_url='signin')
def admin(request):
    return render(request, 'web/admin.html')
def ongezawashiriki(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        # id = request.POST.get('id')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if MyUser.objects.filter(email=email).exists():
                messages.info(request, f"Email {email} Imeshachukuliwa")
                return redirect('ongezawashiriki')
            elif MyUser.objects.filter(username=username).exists():
                messages.info(request, f"Number Ya Ushirika {username} Imeshachukuliwa")
                return redirect('ongezawashiriki')
            else:
                user = MyUser.objects.create_user(username=username, email=email, first_name="Mshiriki", password=password)
                user.save()
                # messages.info(request, 'Registered Student Succesefull.')
                return redirect('washirikipost')
        else:
            messages.info(request, 'Maneno ya siri hayalandani')
            return redirect('ongezawashiriki')

    else:
        return render(request, 'web/ongezawashiriki.html')
    
def ongezaubatizo(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        # id = request.POST.get('id')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if MyUser.objects.filter(email=email).exists():
                messages.info(request, f"Email {email} Imeshachukuliwa")
                return redirect('ongezaubatizo')
            elif MyUser.objects.filter(username=username).exists():
                messages.info(request, f"Number Ya Ushirika {username} Imeshachukuliwa")
                return redirect('ongezaubatizo')
            else:
                user = MyUser.objects.create_user(username=username, email=email, first_name="Ubatizo", password=password)
                user.save()
                # messages.info(request, 'Registered Student Succesefull.')
                return redirect('ubatizopost')
        else:
            messages.info(request, 'Maneno ya siri hayalandani')
            return redirect('ongezaubatizo')

    else:
        return render(request, 'web/ongezaubatizo.html')
    
def ongezashuleyasabato(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        # id = request.POST.get('id')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if MyUser.objects.filter(email=email).exists():
                messages.info(request, f"Email {email} Imeshachukuliwa")
                return redirect('ongezashuleyasabato')
            elif MyUser.objects.filter(username=username).exists():
                messages.info(request, f"Number Ya Ushirika {username} Imeshachukuliwa")
                return redirect('ongezashuleyasabato')
            else:
                user = MyUser.objects.create_user(username=username, email=email, first_name="Shule Ya Yabato", password=password)
                user.save()
                # messages.info(request, 'Registered Student Succesefull.')
                return redirect('shuleyasabatopost')
        else:
            messages.info(request, 'Maneno ya siri hayalandani')
            return redirect('ongezashuleyasabato')

    else:
        return render(request, 'web/ongezashuleyasabato.html')
    
def ongezaviongozi(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if MyUser.objects.filter(email=email).exists():
                messages.info(request, f"Email {email} Imeshachukuliwa")
                return redirect('ongezaviongozi')
            elif MyUser.objects.filter(username=username).exists():
                messages.info(request, f"Number Ya Ushirika {username} Imeshachukuliwa")
                return redirect('ongezaviongozi')
            else:
                user = MyUser.objects.create_user(username=username, email=email, first_name="Kiongozi", password=password)
                user.save()
                # messages.info(request, 'Registered Student Succesefull.')
                return redirect('viongozipost')
        else:
            messages.info(request, 'Maneno ya siri hayalandani')
            return redirect('ongezaviongozi')

    else:
        return render(request, 'web/ongezaviongozi.html')

def signin(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            # messages.info(request, 'Loged in succesefull.')
            return redirect('home')
        else:
            messages.info(request, 'Emaili au neno la siri sio sahihi')
            return redirect('signin')

    else:
        return render(request, 'web/signin.html')

def logout(request):
    auth.logout(request)
    # messages.info(request, 'Loged out succesefull.')
    return redirect('logedout')


def home(request):
    mafundisho = Mafundisho.objects.all()
    matangazo = Matangazo.objects.all()
    context={
        "mafundisho":mafundisho,
        "matangazo":matangazo
    }
    return render(request, 'web/home.html', context)
def aboutus(request):
    return render(request, 'web/aboutus.html')
def base(request):
    return render(request, 'web/base.html')
def contactus(request):
    return render(request, 'web/contactus.html')
def contactpost(request):
    contactpost = ContactForm()
    if request.method == "POST":
        Full_Name = request.POST.get('name')
        Subject = request.POST.get('subject')
        Email = request.POST.get('email')
        Message = request.POST.get('message')
        Phone = request.POST.get('phone')
        contactpost = ContactForm(request.POST, files=request.FILES)
        if contactpost.is_valid():
            contactpost.save()
            messages.info(request, 'Message sent succesefull.')
            return redirect('contactpost')
    context={
        "contactpost":contactpost
    }
    return render(request, 'web/contactpost.html',context)
# @login_required(login_url='signin')
def contactlist(request):
    contactlist = Contact.objects.all()
    countmessage= Contact.objects.all().count()
    context={
        "contactlist":contactlist,
        "countmessage":countmessage
    }
    return render(request, 'web/contactlist.html', context)
# @login_required(login_url='signin')
def viewcontact(request, id):
    contact = Contact.objects.get(id=id)
    
    context = {"contact":contact}
    return render(request, 'web/viewcontact.html', context)
# @login_required(login_url='signin')
def deletecontact(request, id):
    contact = Contact.objects.get(id=id)
    if request.method == "POST":
        contact.delete()
        messages.info(request, 'Message deleted succesefull.')
        return redirect('contactlist')
    
    context = {"contact":contact}
    return render(request, 'web/deletecontact.html', context)


# @login_required(login_url='signin')
def dashboard(request):
    return render(request, 'web/dashboard.html')

def services(request):
    return render(request, 'web/services.html')


# views for success message
def signupsucces(request):
    return render(request, 'web/signupsucces.html')
def logedout(request):
    return render(request, 'web/logedout.html')


def invoices(request):
    return render(request, 'web/invoices.html')
def payments(request):
    return render(request, 'web/payments.html')


def allstaff(request):
    return render(request, 'web/allstaff.html')
def courses(request):
    return render(request, 'web/courses.html')

def certificatecourses(request):
    return render(request, 'web/certificatecourses.html')
def bachelorcourses(request):
    return render(request, 'web/bachelorcourses.html')
def mastercourses(request):
    return render(request, 'web/mastercourses.html')


# viewa for posting
def mafundishopost(request):
    mafundishopost = MafundishoForm()
    if request.method == "POST":
        mafundishopost = MafundishoForm(request.POST, files=request.FILES)
        if mafundishopost.is_valid():
            mafundishopost.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('mafundishopost')
    context={
        "mafundishopost":mafundishopost
    }
    return render(request, 'web/mafundishopost.html',context)

def matangazopost(request):
    matangazopost = MatangazoForm()
    if request.method == "POST":
        matangazopost = MatangazoForm(request.POST, files=request.FILES)
        if matangazopost.is_valid():
            matangazopost.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('matangazopost')
    context={
        "matangazopost":matangazopost
    }
    return render(request, 'web/matangazopost.html',context)

def matukiopost(request):
    matukiopost = MatukioForm()
    if request.method == "POST":
        matukiopost = MatukioForm(request.POST, files=request.FILES)
        if matukiopost.is_valid():
            matukiopost.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('matukiopost')
    context={
        "matukiopost":matukiopost
    }
    return render(request, 'web/matukiopost.html',context)


class viewmatangazo(DetailView):
    model = Matangazo
    template_name = 'web/viewmatangazo.html'
    # count_hit = True
    # HII NI CODES KWA AJILI YA POST DETAIL PAGE KWA KUTUMIA CLASS VIEW ZINAISHIA HAPA

#SASA HIZI ZINAZOANZIA HAPA NI KWA AJILI YA COMMENT KWENYE POST HUSIKA
    form = CommentmatangazoForm

    def post(self, request, *args, **kwargs):
        form = CommentmatangazoForm(request.POST)
        if form.is_valid():
            Title = self.get_object()
            form.instance.user = request.user
            form.instance.Title = Title
            form.save()

            return redirect(reverse("viewmatangazo", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        #kwa ajili ya kudisplay comment huo mstari wa chini
        post_comments = Commentmatangazo.objects.all().filter(Title=self.object.id)
        
        #zinaendelea za kupost comment kwa admin
        context = super().get_context_data(**kwargs)
        #context["form"] = self.form
        context.update({
                'form':self.form,
                'post_comments':post_comments,
                # 'post_comments_count':post_comments_count,
            })
        return context
    
class viewmafundisho(DetailView):
    model = Mafundisho
    template_name = 'web/viewmafundisho.html'
    # count_hit = True
    # HII NI CODES KWA AJILI YA POST DETAIL PAGE KWA KUTUMIA CLASS VIEW ZINAISHIA HAPA

#SASA HIZI ZINAZOANZIA HAPA NI KWA AJILI YA COMMENT KWENYE POST HUSIKA
    form = CommentmafundishoForm

    def post(self, request, *args, **kwargs):
        form = CommentmafundishoForm(request.POST)
        if form.is_valid():
            Title = self.get_object()
            form.instance.user = request.user
            form.instance.Title = Title
            form.save()

            return redirect(reverse("viewmafundisho", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        #kwa ajili ya kudisplay comment huo mstari wa chini
        post_comments = Commentmafundisho.objects.all().filter(Title=self.object.id)
        
        #zinaendelea za kupost comment kwa admin
        context = super().get_context_data(**kwargs)
        #context["form"] = self.form
        context.update({
                'form':self.form,
                'post_comments':post_comments,
                # 'post_comments_count':post_comments_count,
            })
        return context
    
    
class viewmatukio(DetailView):
    model = Matukio
    template_name = 'web/viewmatukio.html'
    # count_hit = True
    # HII NI CODES KWA AJILI YA POST DETAIL PAGE KWA KUTUMIA CLASS VIEW ZINAISHIA HAPA

#SASA HIZI ZINAZOANZIA HAPA NI KWA AJILI YA COMMENT KWENYE POST HUSIKA
    form = CommentmatukioForm

    def post(self, request, *args, **kwargs):
        form = CommentmatukioForm(request.POST)
        if form.is_valid():
            Title = self.get_object()
            form.instance.user = request.user
            form.instance.Title = Title
            form.save()

            return redirect(reverse("viewmatukio", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        #kwa ajili ya kudisplay comment huo mstari wa chini
        post_comments = Commentmatukio.objects.all().filter(Title=self.object.id)
        
        #zinaendelea za kupost comment kwa admin
        context = super().get_context_data(**kwargs)
        #context["form"] = self.form
        context.update({
                'form':self.form,
                'post_comments':post_comments,
                # 'post_comments_count':post_comments_count,
            })
        return context
    
def deletemafundisho(request, id):
    mafundishodelete = Mafundisho.objects.get(id=id)
    if request.method == "POST":
        mafundishodelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('mafundisho')
    
    context = {"mafundishodelete":mafundishodelete}
    return render(request, 'web/deletemafundisho.html', context)

def deletematangazo(request, id):
    matangazodelete = Matangazo.objects.get(id=id)
    if request.method == "POST":
        matangazodelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('matangazo')
    
    context = {"matangazodelete":matangazodelete}
    return render(request, 'web/deletematangazo.html', context)

def deletematukio(request, id):
    matukiodelete = Matukio.objects.get(id=id)
    if request.method == "POST":
        matukiodelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('matukio')
    
    context = {"matukiodelete":matukiodelete}
    return render(request, 'web/deletematukio.html', context)

def updatemafundisho(request, id):
    a = Mafundisho.objects.get(id=id)
    mafundisho = MafundishoForm(instance=a)
    if request.method == "POST":
        mafundisho = MafundishoForm(request.POST, files=request.FILES, instance=a)
        if mafundisho.is_valid():
            mafundisho.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('home')
    context = {"mafundisho":mafundisho}
    return render(request, 'web/updatemafundisho.html', context)

def updatematangazo(request, id):
    a = Matangazo.objects.get(id=id)
    matangazo = MatangazoForm(instance=a)
    if request.method == "POST":
        matangazo = MatangazoForm(request.POST, files=request.FILES, instance=a)
        if matangazo.is_valid():
            matangazo.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('home')
    context = {"matangazo":matangazo}
    return render(request, 'web/updatematangazo.html', context)

def updatematukio(request, id):
    d = Matukio.objects.get(id=id)
    matukio = MatukioForm(instance=d)
    if request.method == "POST":
        matukio = MatukioForm(request.POST, files=request.FILES, instance=d)
        if matukio.is_valid():
            matukio.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('matukio')
    context = {"matukio":matukio}
    return render(request, 'web/updatematukio.html', context)

# washiriki
def washiriki(request):
    washiriki = Washiriki.objects.all()
    washirikiidadi = Washiriki.objects.all.count()
    context={
        "washiriki":washiriki,
        "washirikiidadi":washirikiidadi
    }
    return render(request, 'web/washiriki.html', context)
def washirikipost(request):
    washirikipost = WashirikiForm()
    if request.method == "POST":
        washirikipost = WashirikiForm(request.POST, files=request.FILES)
        if washirikipost.is_valid():
            washirikipost.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('ongezawashiriki')
    context={
        "washirikipost":washirikipost
    }
    return render(request, 'web/washirikipost.html',context)

def shuleyasabatopost(request):
    shuleyasabatopost = WashirikiForm()
    if request.method == "POST":
        shuleyasabatopost = WashirikiForm(request.POST, files=request.FILES)
        if shuleyasabatopost.is_valid():
            shuleyasabatopost.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('ongezashuleyasabato')
    context={
        "shuleyasabatopost":shuleyasabatopost
    }
    return render(request, 'web/shuleyasabatopost.html',context)

def ubatizopost(request):
    ubatizopost = WashirikiForm()
    if request.method == "POST":
        ubatizopost = WashirikiForm(request.POST, files=request.FILES)
        if ubatizopost.is_valid():
            ubatizopost.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('ongezaubatizo')
    context={
        "ubatizopost":ubatizopost
    }
    return render(request, 'web/ubatizopost.html',context)

def viongozipost(request):
    viongozipost = WashirikiForm()
    if request.method == "POST":
        viongozipost = WashirikiForm(request.POST, files=request.FILES)
        if viongozipost.is_valid():
            viongozipost.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('ongezaviongozi')
    context={
        "viongozipost":viongozipost
    }
    return render(request, 'web/viongozipost.html',context)

def updatewashiriki(request, id):
    c = Washiriki.objects.get(id=id)
    washiriki = WashirikiForm(instance=c)
    if request.method == "POST":
        washiriki = WashirikiForm(request.POST, files=request.FILES, instance=c)
        if washiriki.is_valid():
            washiriki.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('washiriki')
    context = {"washiriki":washiriki}
    return render(request, 'web/updatewashiriki.html', context)

def deletewashiriki(request, id):
    washirikidelete = Washiriki.objects.get(id=id)
    if request.method == "POST":
        washirikidelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('washiriki')
    
    context = {"washirikidelete":washirikidelete}
    return render(request, 'web/deletewashiriki.html', context)

def mafundisho(request):
    mafundisho = Mafundisho.objects.all()
    context={
        "mafundisho":mafundisho
    }
    return render(request, 'web/mafundisho.html', context)

def matangazo(request):
    matangazo = Matangazo.objects.all()
    context={
        "matangazo":matangazo
    }
    return render(request, 'web/matangazo.html', context)

def matukio(request):
    matukio = Matukio.objects.all()
    context={
        "matukio":matukio
    }
    return render(request, 'web/matukio.html', context)



def washiriki(request):
    washiriki = Washiriki.objects.all()
    context={
        "washiriki":washiriki
    }
    return render(request, 'web/washiriki.html', context)

def shuleyasabato(request):
    shuleyasabato = Washiriki.objects.all()
    context={
        "shuleyasabato":shuleyasabato
    }
    return render(request, 'web/shuleyasabato.html', context)

def ubatizo(request):
    ubatizo = Washiriki.objects.all()
    context={
        "ubatizo":ubatizo
    }
    return render(request, 'web/ubatizo.html', context)

def viongozi(request):
    viongozi = Washiriki.objects.all()
    context={
        "viongozi":viongozi
    }
    return render(request, 'web/viongozi.html', context)
