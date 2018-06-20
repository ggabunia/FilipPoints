from . import views
from django.conf.urls import url, include
from rest_framework import routers
from fp_app import models
from django.urls import path


# router = routers.DefaultRouter()
# router.register(r'people', views.PeopleView)

app_name = 'fp_api'

urlpatterns = [
    path('', views.api_root),
    path('people/', views.PeopleView.as_view(), name = 'people_list'),
    path('people/<int:count>/', views.PeopleView.as_view(), name = 'people_list'),
    path('points/', views.PointsView.as_view(), name = 'points'),
    path('points/<int:count>/', views.PointsView.as_view(), name = 'points'),
    path('add-person/', views.PersonInsertView.as_view(), name = 'add_person'),
    path('add-points/', views.AddPointsView.as_view(), name = 'add_points'),
    path('update-person/', views.UpdatePerson.as_view(), name = 'update_person'),
    path('update-person/<int:pk>', views.UpdatePerson.as_view(), name = 'update_person'),
     # url(r'^', include(router.urls)),
]
