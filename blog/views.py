from django.shortcuts import render
from django.views import generic
from django.db import models
from .models import Post

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    # return Question.objects.filter(
    #         pub_date__lte=timezone.now()
    #     ).order_by('-pub_date')[:5]
    def get_queryset(self):
        return Post.objects.all()
    

class DetailView(generic.DetailView):
    model = Post
    """
    blog/post_detail.html" 템플릿이 지정하지 않으면 자동으로 사용됨.
    """

    def get_queryset(self): # 오버라이드
        
        return Post.objects.all()