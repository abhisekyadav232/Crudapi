from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('StudentApi/', views.LCstudent.as_view()),    
    path('StudentApi/<int:pk>/', views.RDUstudent.as_view())
]
