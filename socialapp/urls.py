from django.urls import path

from . import  views

urlpatterns = [
    path('signup/',views.Signup.as_view(),name='singup'),
    path('plan/',views.ChoosePlan,name='plan')
]