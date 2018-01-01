from django.shortcuts import render
from django.http import Http404
from .models import Post


def post(request, post_id=0):
    if post_id is 0:
        raise Http404()

    try:
        post_q = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404()

    return render(request, 'blog/post.html', {'post': post_q})


def index(request):
    try:
        recent_posts_q = Post.objects.order_by("-publish_date")[0:4]
    except Post.DoesNotExist:
        raise Http404()

    return render(request, 'blog/index.html', {'recent_posts': recent_posts_q})
