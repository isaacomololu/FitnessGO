from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, RegisterView,CustomLoginView, profile
from .forms import LoginForm

#url routes
urlpatterns = [
    path('', home, name='home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', profile, name='users-profile'),

]

