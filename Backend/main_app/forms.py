# forms.py
from django import forms
from .models import Upload_Form, topic_choice, ContactUs_Form


class UploadFormDoc(forms.ModelForm):
    tittle = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'topic-yWV',
            'placeholder': 'Topic'
        })
    )
    image = forms.URLField(
        widget=forms.URLInput(attrs={
            'class': 'uploadimg-LVT',
            'placeholder': 'Image URL'
        })
    )
    topic = forms.ChoiceField(
        choices=topic_choice,
        widget=forms.Select(attrs={
            'class': 'select-topic-gBw',
            'placeholder': 'Select Topic'
        })
    )
    skills = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'skills-TM7',
            'placeholder': 'Skills Used/ Skill Level'
        })
    )
    intro = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'small-intro-ewP',
            'placeholder': 'Small Introduction'
        })
    )
    content = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'big-intro-4kD',
            'placeholder': 'Big Introduction'
        })
    )
    collab_Mail = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'collobrators-CV3',
            'placeholder': 'Collaborators Mail'
        })
    )
    certifiedBy = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'certified-by-nTF',
            'placeholder': 'Certified By'
        })
    )

    class Meta:
        model = Upload_Form
        fields = ('tittle', 'image', 'topic', 'skills', 'intro', 'content', 'collab_Mail', 'certifiedBy')


class ContactUs(forms.ModelForm):
    Name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'input-box full-name-d65',
            'placeholder': 'Full Name'
        })
    )
    Email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'input-box full-name-yJM',
            'placeholder': 'Email-id'
        })
    )
    PhoneNumber = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'input-box full-name-GRs',
            'placeholder': 'Phone Number'
        })
    )
    Topic = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'input-box full-name-TFT',
            'placeholder': 'Topic/Intrest'
        })
    )
    Message = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'input-box full-name-3Df',
            'placeholder': 'Message'
        })
    )

    class Meta:
        model = ContactUs_Form
        fields = ('Name', 'Email', 'PhoneNumber', 'Topic','Message')
    
