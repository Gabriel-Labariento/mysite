from django import forms

from .models import *

class TaskForm(forms.Form): # TaskForm is a subclass now of forms.Form
    class Meta:
        model = Task
        fields = ["name", 'due_date', 'taskgroup', 'task_image']
        widgets = {
            'due_date': forms.TextInput(
                attrs={ 'type': 'datetime-local'}
            )
        }   
   