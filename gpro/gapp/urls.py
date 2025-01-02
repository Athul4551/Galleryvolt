from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
   path('',views.login_user,name='login'),
   path('signin',views.signup,name='signin'),
   path('welcome',views.main,name='main'),
   path('logout',views.logout_g,name='logout'),
   path('add', views.index, name='index'),
   path('deletion/<int:id>',views.delete_g,name='deletion'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)