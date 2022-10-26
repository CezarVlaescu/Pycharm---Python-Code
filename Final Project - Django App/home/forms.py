from django import forms
from .models import Profile, BlogPost

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_no', 'bio', 'image')
     
        
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'slug', 'content', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of the Blog'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Copy Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Text your blog...'}),
        }