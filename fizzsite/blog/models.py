from django.db import models
from django import forms
from django.contrib.auth.models import User

ANSWERS = [(0, 'YES'), (1, 'NO')]
QUESTIONS = ['Do pineapples belong on pizza?','Are hot dogs sandwiches?','Are you a morning person?',
             'Do you have a selfie as your background?', 'Should pizza crusts be eaten first?'
             'Do you sit in a different seat everyday in class to determine the best view?',
             'Is milk poured before cereal?', 'Do Christmas decorations go up right after Halloween?',
             'Should iced coffee be drunk even if it is -10 degrees?']


class Quiz(forms.Form):
    q1 = forms.MultipleChoiceField(choices=ANSWERS)
    q2 = forms.MultipleChoiceField(choices=ANSWERS)
    q3 = forms.MultipleChoiceField(choices=ANSWERS)
    q4 = forms.MultipleChoiceField(choices=ANSWERS)
    q5 = forms.MultipleChoiceField(choices=ANSWERS)
    q6 = forms.MultipleChoiceField(choices=ANSWERS)
    q7 = forms.MultipleChoiceField(choices=ANSWERS)
    q8 = forms.MultipleChoiceField(choices=ANSWERS)
    q9 = forms.MultipleChoiceField(choices=ANSWERS)
    q10 = forms.MultipleChoiceField(choices=ANSWERS)
