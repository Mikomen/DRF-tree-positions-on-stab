from django.urls import path,include
from rest_framework import routers
from main import views

router = routers.DefaultRouter()
router.register(r'position', views.PositionViewSet)
router.register(r'level', views.LevelViewSet)
router.register(r'all_employers', views.EmployerViewSet)
router.register(r'stab_employer', views.FullEmployerViewSet)



urlpatterns= [
    path('',include(router.urls))
]
