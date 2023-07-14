from django.contrib import admin
from django.urls import path, include
from core.views import index, role
from django.contrib.auth import views
from userprofile.views import signup
from userprofile.forms import LoginForm


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('sign-up/', signup, name='signup'),
    path('log-in/', views.LoginView.as_view(template_name='userprofile/login.html', authentication_form=LoginForm), name='login'),
    path('role/', role, name='role'),
    path('news/', include('test_autor.urls')),
]
