from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

# creat routers
router = DefaultRouter()

# register Studentviewset with router.
router.register('studentapi', views.studentviewset,basename='student')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
