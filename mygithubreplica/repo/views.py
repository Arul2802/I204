from django.shortcuts import render, get_object_or_404, redirect
from .models import Repository, File, Commit
from .forms import RepositoryForm, FileForm, CommitForm

def repo_list(request):
    repositories = Repository.objects.all()
    return render(request, 'repo_list.html', {'repositories': repositories})

def repo_detail(request, repo_id):
    repository = get_object_or_404(Repository, id=repo_id)
    return render(request, 'repo_detail.html', {'repository': repository})

def add_repo(request):
    if request.method == 'POST':
        form = RepositoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('repo_list')
    else:
        form = RepositoryForm()
    return render(request, 'add_repo.html', {'form': form})

def add_file(request, repo_id):
    repository = get_object_or_404(Repository, id=repo_id)
    if request.method == 'POST':
        form = FileForm(request.POST)
        if form.is_valid():
            file = form.save(commit=False)
            file.repository = repository
            file.save()
            return redirect('repo_detail', repo_id=repository.id)
    else:
        form = FileForm()
    return render(request, 'add_file.html', {'form': form, 'repository': repository})

def commit_changes(request, repo_id):
    repository = get_object_or_404(Repository, id=repo_id)
    if request.method == 'POST':
        form = CommitForm(request.POST)
        if form.is_valid():
            commit = form.save(commit=False)
            commit.repository = repository
            commit.save()
            form.save_m2m()
            return redirect('repo_detail', repo_id=repository.id)
    else:
        form = CommitForm()
    return render(request, 'commit_changes.html', {'form': form, 'repository': repository})