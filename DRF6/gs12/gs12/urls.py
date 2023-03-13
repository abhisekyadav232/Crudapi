from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('StudentApi/', views.liststudent.as_view()),
    # path('StudentApi/', views.studentcreate.as_view()),
    # path('StudentApi/<int:pk>/', views.studentRetrive.as_view()),
    # path('StudentApi/<int:pk>/', views.studentupdate.as_view()),
    # path('StudentApi/<int:pk>/', views.studentDestroy.as_view()),
    # path('StudentApi/', views.LCstudent.as_view()),
    # path('StudentApi/<int:pk>/', views.RDstudent.as_view())
    path('StudentApi/<int:pk>/', views.RDUstudent.as_view())
]
