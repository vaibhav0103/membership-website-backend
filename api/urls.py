from django.urls import path
from .views import course_list, course_detail
from users.views import register_user, logout_by_blacklist, user_details, enroll_user, user_enrolled_courses
  
urlpatterns = [
    path('courses/', course_list, name = 'course-list'),
    path('course/<slug:slug>/', course_detail, name = 'course-detail'),
    path('user/register/', register_user, name='register-user'),
    path('user/logout/', logout_by_blacklist, name='blacklist'),
    path('user/profile/', user_details),
    path('user/enroll/', enroll_user),
    path('user/courses/', user_enrolled_courses),
    
]