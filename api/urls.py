from django.urls import path
from .views import CourseListView, CourseDetailView

urlpatterns = [
    
    path("mix/api/", CourseListView.as_view() ),
    path("mix/api/<int:pk>", CourseDetailView.as_view() ),
]
