"""
URL configuration for happywedding project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from weddingapp import views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
     path('login/',views.login,name='login'),
    path('loginhome/',views.loginhome,name='loginhome'),
    path('logout/',views.handlelogout,name='handlelogout'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('adminfirst/',views.adminfirst,name="adminfirst"),
    path('vendorhome/',views.vendorhome,name="vendorhome"),
    path("adminhome/",views.adminhome,name="adminhome"),
    path("create_user/",views.create_user,name="create_user"),
    path('update_profile/',views.update_profile,name="update_profile"),
    path('change_password/', views.change_password, name='change_password'),
    path('activate_user/<int:user_id>/', views.activate_user, name='activate_user'),
    path('deactivate_user/<int:user_id>/', views.deactivate_user, name='deactivate_user'),
    path('verify/<str:verification_code>/', views.verify_email, name='verify_email'),
    path('gold_booking/',views.gold_booking,name="gold_booking"),
    path('silver_booking/',views.silver_booking,name="silver_booking"),
    path('platinum_booking/',views.platinum_booking,name="platinum_booking"),
    path('confirmation/', views.confirmation_view, name='confirmation'),
    path('cancellation/', views.cancellation_view, name='cancellation'),
    path('gold/',views.gold,name='gold'),
    path('silver/',views.silver,name='silver'),
    path('platinum/',views.platinum,name='platinum'),
    path('customise/',views.customise,name='customise'),
    path('toggle-booking/<int:booking_id>/', views.toggle_booking_gold, name='toggle_booking_gold'),
    path('toggle-booking-silver/<int:booking_id>/', views.toggle_booking_silver, name='toggle_booking_silver'),
    path('toggle-booking-platinum/<int:booking_id>/', views.toggle_booking_platinum, name='toggle_booking_platinum'),
    path('toggle-booking-customise/<int:booking_id>/', views.toggle_booking_customise, name='toggle_booking_customise'),
     path('view_profile/', views.view_profile, name='view_profile'),
      path('cancel_package_gold/<int:package_id>/', views.cancel_package_gold, name='cancel_package_gold'),
       path('cancel_package_silver/<int:package_id>/', views.cancel_package_silver, name='cancel_package_silver'),
        path('cancel_package_platinum/<int:package_id>/', views.cancel_package_platinum, name='cancel_package_platinum'),
        path('cancel_package_customise/<int:package_id>/', views.cancel_package_customise, name='cancel_package_customise'),
    path('customise_booking/',views.customise_booking,name="customise_booking"),    
]



   






