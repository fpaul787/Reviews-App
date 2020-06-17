from django import forms
from .models import Comment

class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = Comment
        fields = ['content']

