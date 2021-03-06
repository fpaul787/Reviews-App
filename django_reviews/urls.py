from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.urls import path, include, re_path
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name="register"),
    path('profile/', user_views.profile, name="profile"),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', user_views.logout, name="logout"),
    path('password-reset/',
    auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),
    name='password_reset'),
    path('password-reset/done/', 
    auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), 
    name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', 
    auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), 
    name='password_reset_confirm'),
    path('password-reset-complete/',
    auth_views.PasswordResetView.as_view(template_name="users/password_reset_complete.html"),
    name='password_reset_complete'),    
    path('', RedirectView.as_view(url="/home")),
    path('', include('reviews.urls'))
    
]
handler404 = 'error.views.handler404'
# handler500 = Myhandler500

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document=settings.STATIC_ROOT)