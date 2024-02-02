from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin, name = "admin"),
    path('ongezawashiriki/', views.ongezawashiriki, name = "ongezawashiriki"),
    path('ongezaubatizo/', views.ongezaubatizo, name = "ongezaubatizo"),
    path('ongezashuleyasabato/', views.ongezashuleyasabato, name = "ongezashuleyasabato"),
    path('ongezaviongozi/', views.ongezaviongozi, name = "ongezaviongozi"),
    path('signin/', views.signin, name = "signin"),
	path('logout/', views.logout, name="logout"),
 
    path("",views.home,name = "home"),
    path("aboutus/",views.aboutus,name = "aboutus"),
    path("base/",views.base,name = "base"),
    path("contactus/",views.contactus,name = "contactus"),
    path("contactpost/",views.contactpost,name = "contactpost"),
    path("contactlist/",views.contactlist,name = "contactlist"),
    path("viewcontact/<int:id>/",views.viewcontact,name = "viewcontact"),
    path('deletecontact/<int:id>/', views.deletecontact, name = "deletecontact"),
    path("dashboard/",views.dashboard,name = "dashboard"),
    path("services/",views.services,name = "services"),
    
    # url for success message
    path("signupsucces/",views.signupsucces,name = "signupsucces"),
    path("logedout/",views.logedout,name = "logedout"),
    
    
    path("invoices/",views.invoices,name = "invoices"),
    path("payments/",views.payments,name = "payments"),
    
    
    path("allstaff/",views.allstaff,name = "allstaff"),
    path("courses/",views.courses,name = "courses"),
    
    path("certificatecourses/",views.certificatecourses,name = "certificatecourses"),
    path("bachelorcourses/",views.bachelorcourses,name = "bachelorcourses"),
    path("mastercourses/",views.mastercourses,name = "mastercourses"),
    
    # urls for church
    path("mafundishopost/",views.mafundishopost,name = "mafundishopost"),
    path("matangazopost/",views.matangazopost,name = "matangazopost"),
    path("matukiopost/",views.matukiopost,name = "matukiopost"),

    path('viewmatangazo/<str:pk>/', views.viewmatangazo.as_view(), name = "viewmatangazo"),
    path('viewmafundisho/<str:pk>/', views.viewmafundisho.as_view(), name = "viewmafundisho"),
    path('viewmatukio/<str:pk>/', views.viewmatukio.as_view(), name = "viewmatukio"),
    
    path('deletemafundisho/<int:id>/', views.deletemafundisho, name = "deletemafundisho"),
    path('deletematangazo/<int:id>/', views.deletematangazo, name = "deletematangazo"),
    path('deletematukio/<int:id>/', views.deletematukio, name = "deletematukio"),
    
    path('updatemafundisho/<int:id>/', views.updatemafundisho, name = "updatemafundisho"),
    path('updatematangazo/<int:id>/', views.updatematangazo, name = "updatematangazo"),
    path('updatematukio/<int:id>/', views.updatematukio, name = "updatematukio"),
    
    
    # urls for washiriki
    path("washiriki/",views.washiriki,name = "washiriki"),
    path("washirikipost/",views.washirikipost,name = "washirikipost"),
    path("shuleyasabatopost/",views.shuleyasabatopost,name = "shuleyasabatopost"),
    path("ubatizopost/",views.ubatizopost,name = "ubatizopost"),
    path("viongozipost/",views.viongozipost,name = "viongozipost"),
    
    path('deletewashiriki/<int:id>/', views.deletewashiriki, name = "deletewashiriki"),
    
    path('updatewashiriki/<int:id>/', views.updatewashiriki, name = "updatewashiriki"),
    
    path("mafundisho/",views.mafundisho,name = "mafundisho"),
    path("matangazo/",views.matangazo,name = "matangazo"),
    path("matukio/",views.matukio,name = "matukio"),
]
