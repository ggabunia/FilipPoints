from django.urls import path
from django.contrib.auth import views as auth_views
from manager import views

app_name = 'manager'

urlpatterns =[

    path('login/', auth_views.LoginView.as_view(template_name='manager/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('new/', views.PersonCreate.as_view(), name = 'new'),
    path('edit/<int:pk>/', views.PersonEdit.as_view(), name = "edit"),
    path('add-points/<int:pk>/', views.AddPoints.as_view(), name = "add_points"),
    path('delete/<int:pk>/',views.DeletePerson.as_view(), name='delete'),
    path('remove-points/<int:pk>/',views.RemovePoints.as_view(), name = 'remove_points'),

]
