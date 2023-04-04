from django.shortcuts import render
from rest_framework import mixins, generics
from .models import  Course
from .serializers import CourseSerializer


# Create your views here.
class CourseListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    
    
    
    
    
    
    
class CourseDetailView(generics.GenericAPIView, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    
    def get(self, request, pk):
        return self.retrieve(request)
    
    def update(self, request, pk):
        return self.update(request, pk)
    
    def destroy(self, request, pk):
        return self.destroy(request, pk)
    