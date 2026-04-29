from django.urls import path
from . import views

app_name = 'blog' # Пространство имен, чтобы не путать с другими аппками

urlpatterns = [
#     # === 1. Маршруты для всех (Guests) ===
#     path('', views.post_list, name='post_list'),                 # GET: Лента всех постов (с пагинацией)
#     path('<int:post_id>/', views.post_detail, name='post_detail'), # GET: Деталка поста + список комментов
#
#     # === 2. Маршруты интерактива (Залогиненные) ===
#     path('<int:post_id>/comment/', views.add_comment, name='add_comment'), # POST: Добавить коммент
#     path('<int:post_id>/like/', views.toggle_like, name='toggle_like'),    # POST: Поставить/убрать лайк
#
#     # === 3. Маршруты Автора (CRUD) ===
#     path('create/', views.post_create, name='post_create'),                # GET/POST: Создать
#     path('<int:post_id>/edit/', views.post_update, name='post_update'),    # GET/POST: Редактировать
#     path('<int:post_id>/delete/', views.post_delete, name='post_delete'),  # POST: Удалить
]