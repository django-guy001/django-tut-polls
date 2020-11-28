from django import forms

from . import models


class QuestionForm(forms.ModelForm):
    choice = forms.ModelChoiceField(
        label='',
        queryset=models.Choice.objects.all(),
        widget=forms.RadioSelect)

    class Meta:
        model = models.Question
        fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['choice'].queryset = self.instance.choice_set.all()

    def save_selected_choice(self):
        self.cleaned_data['choice'].votes += 1
        self.cleaned_data['choice'].save(update_fields=['votes'])
