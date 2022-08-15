
from django import forms
from django.core.exceptions import ValidationError

class TextForm(forms.Form):
  text = forms.CharField(label='', widget=forms.Textarea)
  search = forms.CharField(label='検索')
  replace = forms.CharField(label='置換')
  
  def clean(self):
    data = super().clean()
    text = data['text']
    if len(text) <= 5:
      raise ValidationError('テキストが短すぎます。6文字以上入力してください。')
    return data
  

from .models import Post

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'body']