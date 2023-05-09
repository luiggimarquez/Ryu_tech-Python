from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path("", views.base, name="home"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.log_out, name= "logout"),
    path("login/", views.log_in , name = "login"),
    path("profile/", views.profile, name = "profile"),
    path("user/edit/", views.edituser,  name = "edituser"),
    path("profile/edit/", views.editprofile.as_view(), name = "editprofile")
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)