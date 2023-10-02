from django.db import models
from accounts.models import User
from django.conf import settings



class Blog(models.Model):
    
    title       = models.CharField(max_length=40)
    content     = models.TextField()
    author      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"


    def __str__(self) -> str:
        """
        Unicode representation of blog model.
        """
        return self.title