from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('StudentApi/', views.LCStudentApi.as_view()),
    # path('StudentApi/', views.Student_list.as_view()),
    # path('StudentApi/<int:pk>/', views.StudentUpdate.as_view()),
    path('RUDStudentApi/<int:pk>/', views.RUDStudentApi.as_view()),
]
