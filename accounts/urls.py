from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='accounts'

urlpatterns = [
    path('signup_poke/',views.SignupPokeView.as_view(),name='signup_poke'),
    path('signup_poke_success/',views.SignupPokeSuccessView.as_view(),name='signup_poke_success'),
    path('logout_poke/',auth_views.LogoutView.as_view(template_name='logout_poke.html'),name='logout_poke'),
    path('login_poke/',auth_views.LoginView.as_view(template_name='login_poke.html'), name='login_poke'),
]
