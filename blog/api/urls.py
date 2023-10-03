from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

urlpatterns = [
    path('', BlogListView.as_view()),
    path('create/', BlogCreateView.as_view()),
    path('<int:pk>/', BlogDetailView.as_view()),  
    path('<int:pk>/update/', BlogUpdateDeleteView.as_view()),   
    path('<int:pk>/delete/', BlogUpdateDeleteView.as_view()),   

]

urlpatterns = format_suffix_patterns(urlpatterns)