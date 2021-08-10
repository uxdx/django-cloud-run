from django.db import models

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=100, unique=True) # 제목
    post_contents = models.TextField() # 내용
    pub_date = models.DateTimeField('date published') #발행일

    def __str__(self):
        return self.post_title
    