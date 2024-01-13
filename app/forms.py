from django import forms
from app.models import *
from django.core import validators

def TopicForm_validate(data):
    if data.lower().startswith('a'):
        raise forms.ValidationError('1-Invalid Data')


def TopicForm_validate2(dataa):
    if len(dataa)<6:
        raise forms.ValidationError('2-Invalid Data')

class TopicForm(forms.Form):
    Topic_name=forms.CharField(validators=[TopicForm_validate,TopicForm_validate2])


class WebPageForm(forms.Form):
    tl=[[to.Topic_name,to.Topic_name] for to in Topic.objects.all()]
    Topic_name=forms.ChoiceField(choices=tl)
    Name=forms.CharField()
    Email=forms.EmailField()
    Url=forms.URLField()
    BotCacher=forms.CharField(required=False,widget=forms.HiddenInput)


    def clean_BotCacher(self):
        b=self.cleaned_data['BotCacher']
        if len(b)>0:
            raise forms.ValidationError('invalid data')


class AccessRecordForm(forms.Form):
    wl=[[wo.pk,wo.Name] for wo in WebPage.objects.all()]
    Name=forms.ChoiceField(choices=wl)
    Author=forms.CharField()
    Date=forms.DateField()