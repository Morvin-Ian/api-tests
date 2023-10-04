from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

urlpatterns = [
    path('', BlogListView.as_view(), name="blog-list"),
    path('create/', BlogCreateView.as_view(), name="blog-create"),
    path('<int:pk>/', BlogDetailView.as_view(), name="blog-detail"),  
    path('<int:pk>/update/', BlogUpdateDeleteView.as_view(), name="blog-update"),   
    path('<int:pk>/delete/', BlogUpdateDeleteView.as_view(), name="blog-delete"),   

]

urlpatterns = format_suffix_patterns(urlpatterns)