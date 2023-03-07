from django import forms
from django.core.exceptions import ValidationError
from webapp.models import Issue
from django.core.validators import MaxLengthValidator, MinLengthValidator


def min_len_validator(string):
    if len(string) < 2:
        raise ValidationError('Заголовок должен быть длинее 2-ух символов')
    return string


def letters_capital_validator(string):
    if string != string.capitalize():
        raise ValidationError('Строка должна начинаться с большой буквы')


class IssueForm(forms.ModelForm):
    summary = forms.CharField(validators=(MaxLengthValidator(
        limit_value=50,
    ), min_len_validator, letters_capital_validator))
    description = forms.CharField(widget=forms.Textarea, validators=(MinLengthValidator(
        limit_value=2,
    ), letters_capital_validator))

    class Meta:
        model = Issue
        fields = ('summary', 'description', 'status', 'type')
        labels = {
            'summary': 'Заголовок задачи',
            'description': 'Описание задачи',
            'status': 'Статус',
            'type': 'Тип'
        }
