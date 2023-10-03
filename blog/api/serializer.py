from rest_framework import serializers
from blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    """
    Serializer for the Blog Model
    """
    class Meta:
        model = Blog
        fields = (
            'id',
            'author', 
            'title', 
            'content', 
            'created_at', 
        )
        read_only_fields = ['id', 'author','created_at']

        
