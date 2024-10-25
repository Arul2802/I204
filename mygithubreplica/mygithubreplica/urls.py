from django.contrib import admin
from django.urls import path
from repo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.repo_list, name='repo_list'),  # Root URL will show the list of repositories
    path('add_repo/', views.add_repo, name='add_repo'),  # URL to add a new repository
    path('repository/<int:repo_id>/', views.repo_detail, name='repo_detail'),  # Detail view for a repository
    path('repository/<int:repo_id>/add_file/', views.add_file, name='add_file'),  # Add file to repository
    path('repository/<int:repo_id>/commit/', views.commit_changes, name='commit_changes'),  # Commit changes to repository
]
