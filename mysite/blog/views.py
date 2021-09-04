from django.views import generic
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    template_name = "index.html"
    def get_queryset(self):
        return Post.objects.filter(status = 1).order_by('-created_on')
    

class PostDetail(generic.DetailView):
    model = Post
    template_name = "post_detail.html"