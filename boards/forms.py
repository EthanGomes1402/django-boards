from django import forms
from .models import Topic, Post, Contact


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
          attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
        ),
        max_length=4000,
        help_text='Max length of the text is 4000.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']


class PostForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'placeholder': 'Enter reply'}), max_length=4000)

    class Meta:
        model = Post
        fields = ['message' ]


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.Textarea(attrs={'rows': 1}))
    email = forms.CharField(widget=forms.Textarea(attrs={'rows': 1}))
    query = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'placeholder': 'Enter your query'}), max_length=500)

    class Meta:
        model = Contact
        fields = ['name','email','query']

