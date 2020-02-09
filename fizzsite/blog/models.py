from django.db import models
from django import forms
from django.contrib.auth.models import User

ANSWERS = [(0, 'YES'), (1, 'NO')]

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
