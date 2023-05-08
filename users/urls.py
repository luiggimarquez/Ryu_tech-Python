from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path("", views.base, name="home"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.log_out, name= "logout"),
    path("login/", views.log_in , name = "login"),
    path("profile/", views.profile.as_view(), name = "profile")
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)