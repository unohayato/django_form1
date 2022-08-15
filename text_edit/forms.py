
from django import forms
from django.core.exceptions import ValidationError

class TextForm(forms.Form):
  text = forms.CharField()
  search = forms.CharField()
  replace = forms.CharField()
  
  def clean(self):
    data = super().clean()
    text = data['text']
    if len(text) <= 5:
      raise ValidationError('テキストが短すぎます。6文字以上入力してください。')
    return data