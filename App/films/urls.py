from django.urls import path, include
from films import views
from django.contrib.auth.views import LogoutView
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('', views.IndexView.as_view(), name='home'), 
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'), 
    path("register/", views.RegisterView.as_view(), name="register"),
    path("tasks/", views.TasksList.as_view(), name="tasks"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




htmx_urlpatterns = [
    path("check-username/", views.check_username, name='check-username'),
    path('add-task/', views.add_task, name='add-task'),
    path('delete-task/<int:pk>/', views.delete_task, name='delete-task'),
    path('search-task/', views.search_task, name='search-task'),
    path('clear/', views.clear, name='clear'),
    path('sort/', views.sort, name='sort'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('task-list-partial/', views.task_list_partial, name='task-list-partial'),
    path('upload-photo/<int:pk>', views.upload_photo, name='upload-photo'),
    
]

urlpatterns += htmx_urlpatterns

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]