from django.urls import path
from .views import course_list, course_detail
  
urlpatterns = [
    path('courses/', course_list, name = 'course-list'),
    path('course/<slug:slug>/', course_detail, name = 'course-detail'),
]