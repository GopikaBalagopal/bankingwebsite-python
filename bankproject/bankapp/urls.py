
from django.urls import path
from . import views
from .views import DistrictsView, BranchesView

app_name = 'bank'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('details/', views.details, name='details'),
    path('welcome/', views.welcome, name='welcome'),
    path('products/<int:products_id>/',views.about,name='about'),
    # path('registration_form/', views.registration_form, name='registration_form'),
    # path('detail/', views.detail, name='detail'),
    # path('submit_registration/', views.submit_registration, name='submit_registration'),
    path('api/districts/', DistrictsView.as_view(), name='districts_api'),
    path('api/branches/', BranchesView.as_view(), name='branches_api'),


]


