from django.urls import path
from fp_app import views

app_name = 'filip_points'

urlpatterns =[
    path('', views.Index.as_view(), name = 'index'),
    path('all/', views.PersonList.as_view(), name = 'all'),
    path('details/<int:pk>/', views.PersonDetail.as_view(), name = "details"),

]
