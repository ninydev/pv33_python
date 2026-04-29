from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from .models import Post, Comment
from .forms import PostForm, CommentForm

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
    form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': form
    })

@login_required
@require_POST
def add_comment(request, post_id):
    """
    Добавляет новый комментарий к посту.
    """
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.author = request.user
        comment.save()
    
    return redirect('blog:post_detail', post_id=post.id)

@login_required
def post_create(request):
    """
    Создание нового поста. Доступно только авторизованным пользователям.
    """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_list')
    else:
        form = PostForm()
    
    return render(request, 'blog/post_create.html', {'form': form})

@login_required
def post_update(request, post_id):
    """
    Редактирование существующего поста. Только для автора поста.
    """
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user:
        raise PermissionDenied
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'blog/post_update.html', {'form': form, 'post': post})

@login_required
def post_delete(request, post_id):
    """
    Удаление поста. Только для автора поста.
    """
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user:
        raise PermissionDenied
    
    if request.method == 'POST':
        post.delete()
        return redirect('blog:post_list')
    
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

@login_required
@require_POST
def toggle_like(request, post_id):
    """
    Ставит или убирает лайк под постом (AJAX).
    """
    post = get_object_or_404(Post, id=post_id)
    
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
        
    return JsonResponse({
        'likes_count': post.total_likes(),
        'liked': liked
    })
