from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('pricing/', views.pricing, name='pricing'),
    path('reg_form/', views.reg_form, name='reg_form'),
    path('bookings/', views.bookings, name='bookings'), #displays all available lessons teaching any instrument
    path('bookings_Piano/', views.bookings_Piano, name='bookings_Piano'), #displays lessons for Piano
    path('bookings_Claranet/', views.bookings_Claranet, name='bookings_Claranet'), #displays lessons for Claranet
    path('bookings_Flute/', views.bookings_Flute, name='bookings_Flute'), #displays lessons for flute
    path('bookings_Violin/', views.bookings_Violin, name='bookings_Violin'), #displays lessons for Violin
    path('bookings_Guitar/', views.bookings_Guitar, name='bookings_Guitar'), #displays lessons for Guitar
    path('bookings_Trumpet/', views.bookings_Trumpet, name='bookings_Trumpet'), #displays lessons for Trumpet
    path('bookings_English/', views.bookings_English, name='bookings_English'),
    path('bookings_Spanish/', views.bookings_Spanish, name='bookings_Spanish'),
    path('bookings_Italian/', views.bookings_Italian, name='bookings_Italian'),
    path('bookings_German/', views.bookings_German, name='bookings_German'),
    path('bookings_Chinese/', views.bookings_Chinese, name='bookings_Chinese'),
    path('bookings_French/', views.bookings_French, name='bookings_French'),
    path('lessons/', views.lessons, name='lessons'),
    path('instrument/', views.instrument, name='instrument'),
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('account/', views.account, name='account'),
    path('account/login/', views.account, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp, name='signup'),
    path('account/edit/', views.edit_account, name='edit_account'),
    # path('account/profile/', views.Profile, name='profile')
    path('teacher_details/', views.teacher_details, name='teacher_details'),
]
