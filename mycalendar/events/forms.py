from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['FIO', 'phone', 'group', 'email', 'is_marked_10', 'is_marked_11', 'is_marked_12', 'is_marked_13',
                  'is_marked_14', 'is_marked_16']

    def clean(self):
        cleaned_data = super().clean()
        required_fields = ['FIO', 'phone', 'email']
        bool_fields = ['is_marked_10', 'is_marked_11', 'is_marked_12', 'is_marked_13', 'is_marked_14', 'is_marked_16']
        for field in required_fields:
            if not cleaned_data.get(field):
                self.add_error(field, "Введите данные")
        count = 0
        for field in bool_fields:
            if cleaned_data.get(field):
                count += 1
        if count == 0:
            self.add_error('is_marked_10', "Выберите время консультации. ")
        if count > 1:
            self.add_error('is_marked_10', "Выберите только одно время консультации. ")
        return cleaned_data
