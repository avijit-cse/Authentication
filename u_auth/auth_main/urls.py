from django.urls import path
from auth_main import views
from django.conf import settings
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns

app_name='auth_main'

urlpatterns = [
    path("",views.index,name="index"),
    path("reg/",views.registartion,name="registartion"),
    path("login/",views.Login_page,name="Login_page"),
    path("userlogout/",views.user_logout,name="user_logout"),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
 


