from django.urls import path
from .views import EmployeeView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'employees', EmployeeView, basename='employees')
urlpatterns = router.urls