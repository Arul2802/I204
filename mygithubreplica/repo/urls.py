from django.urls import path
from . import views

urlpatterns = [
    path('repository/<int:repo_id>/add_file/', views.add_file, name='add_file'),
    path('repository/<int:repo_id>/commit/', views.commit_changes, name='commit_changes'),
    path('repository/<int:repo_id>/', views.repo_detail, name='repo_detail'),
]
