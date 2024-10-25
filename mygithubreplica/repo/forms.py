from django import forms
from .models import File, Repository, Commit

class RepositoryForm(forms.ModelForm):
    class Meta:
        model = Repository
        fields = ['name', 'description']

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'content']

class CommitForm(forms.ModelForm):
    class Meta:
        model = Commit
        fields = ['message', 'files']
