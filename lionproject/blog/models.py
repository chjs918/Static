from django.db import models

# Create your models here.

class Blog(models.Model):   
    blog_title = models.CharField(max_length=200)
    blog_writer = models.CharField(max_length=100)
    blog_date = models.DateTimeField()
    blog_body = models.TextField()
  

    def __str__(self):
          return self.blog_title

    def blog_summary(self):
        return self.blog_body[:100]