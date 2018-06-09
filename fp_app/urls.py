from django.urls import path
from fp_app import views

app_name = 'filip_points'

urlpatterns =[
    path('', views.PersonList.as_view(), name = 'index'),
    path('details/<int:pk>/', views.PersonDetail.as_view(), name = "details"),

]
