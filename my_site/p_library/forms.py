from django import forms  
from p_library.models import *  
from django.forms import formset_factory  
  
class AuthorForm(forms.ModelForm):  
  
    full_name = forms.CharField(widget=forms.TextInput)  
  
    class Meta:  
        model = Author  
        fields = '__all__'  
  
  
class BookForm(forms.ModelForm):  
    class Meta:  
        model = Book  
        fields = '__all__'
class FriendCreateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Friend
        fields = "__all__"