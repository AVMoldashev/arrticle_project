from django import forms
from django.forms import widgets
from webapp.models import Tag, Article
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

def at_least_5(string):
    if len(string) < 5:
        raise ValidationError('Поле не может быть короче 5 символов')


class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=50, required=True, validators=(at_least_5,), label="Название" )
    class Meta:
        model = Article
        fields = ('title', 'author', 'content', 'tags')
        widgets = {
            'tags': widgets.CheckboxSelectMultiple()
        }


#class ArticleForm(forms.Form):
#    title = forms.CharField(max_length=50, required=True, #validators=(at_least_5,),
#                            validators=(MinLengthValidator(5),),
#                            label="Название")
#    content = forms.CharField( required=True, label="Текст", widget=widgets.Textarea)
#    author = forms.CharField(max_length=50, required=True, label="Автор")
#    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), label="Теги", required=True)


    #def clean_title(self):
    #    title = self.clean_data["title"]
    #    if len(title)<5:
    #        raise ValidationError('Поле не может быть короче 5 символов')

    def clean(self):
         title = self.cleaned_data.get('title')
         content = self.cleaned_data.get('content')
         if title and content and title == content:
             raise ValidationError('Заголовок и контент не могут быть равны')

         return super().clean()