from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Comment

def post_list(request):
    """
    Отображает список всех постов с пагинацией.
    """
    posts_list = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts_list, 5)  # Показывать по 5 постов на странице

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/post_list.html', {'page_obj': page_obj})

def post_detail(request, post_id):
    """
    Отображает детальную информацию о посте и список комментариев к нему.
    """
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by('-created_at')

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments
    })
