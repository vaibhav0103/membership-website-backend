from django.urls import path
from .views import course_list, course_detail
from users.views import register_user, logout_by_blacklist, check_user
  
urlpatterns = [
    path('courses/', course_list, name = 'course-list'),
    path('course/<slug:slug>/', course_detail, name = 'course-detail'),
    path('user/register/', register_user, name='register-user'),
    path('user/logout/', logout_by_blacklist, name='blacklist'),
    path('user/is_authenticated/', check_user),
]