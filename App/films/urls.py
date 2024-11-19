from django.urls import path
from films import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("tasks/", views.TasksView.as_view(), name="tasks"),
]




htmx_urlpatterns = [
    path("check-username/", views.check_username, name='check-username'),
    path('add-task/', views.add_task, name='add-task'),
    path('delete-task/<int:pk>/', views.delete_task, name='delete-task'),
    path('search-task/', views.search_task, name='search-task'),
    path('clear/', views.clear, name='clear'),
    #path('sort/', views.sort, name='sort'),
    
]

urlpatterns += htmx_urlpatterns