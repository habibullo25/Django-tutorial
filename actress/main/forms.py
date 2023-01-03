from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from django.core.exceptions import ValidationError

class AddPostForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['cat'].empty_label = 'CAtegory does not select'
    # title = forms.CharField(max_length=255,label="Zagolovok",widget=forms.Textarea(attrs={'class':"form-input"}))
    # slug = forms.SlugField(max_length=255,label="URL")
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':10}),label="Text")
    # is_published = forms.BooleanField(label="Publikatsiya",required=False,initial=True)
    # cat = forms.ModelChoiceField(queryset=Category.objects.all(),label="Kategoriya",empty_label="kategoriya ne vibrana")
    class Meta:
        model = Women
        # fields="__all__"
        fields = ['title','slug','photo','content','is_published','cat']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-input'}),
            'content':forms.Textarea(attrs={'cols':60,'rows':10}),
        }
        
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title)>200:
            raise ValidationError('too long')
        return title
    
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='login',widget=forms.TextInput(attrs={'class':'form-input'}))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'form-input'}))
    password1 = forms.CharField(label='Parol',widget=forms.TextInput(attrs={'class':'form-input'}))
    password2 = forms.CharField(label='repeat parol',widget=forms.TextInput(attrs={'class':'form-input'}))
    
    class Meta:
        model = User
        fields = {'username','email','password1','password2'}
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-input'}),
            'password1': forms.PasswordInput(attrs={'class':'form-input'}),
            'password2': forms.PasswordInput(attrs={'class':'form-input'}),
            
            
        }
        
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-input'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-input'}))
        