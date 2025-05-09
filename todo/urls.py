from django.urls import path
from todo import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_task', views.add_task, name='add_task'),
    path('delete_task/<int:task_id>', views.delete_task, name='delete_task'),
    path('logout', views.logout_view, name='logout'),
    path('login', views.login_view, name='login'),
    path('toggle_star/<int:task_id>/', views.toggle_star, name='toggle_star'),
    path('abc/', views.abc, name='abc'),
    path('favourites/', views.favourites, name='favourites'),
    path('register', views.register, name='register'),
]
