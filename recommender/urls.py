from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('recommend/', views.recommend_view, name='recommend'),
    path('result/<int:pk>/', views.result_view, name='result'),
    path('result/<int:pk>/feedback/', views.submit_feedback, name='submit_feedback'),
    path('result/<int:pk>/delete/', views.delete_recommendation, name='delete_recommendation'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses_list, name='courses'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('search/', views.search_view, name='search'),
]
