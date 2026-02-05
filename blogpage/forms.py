from django import forms

class TaskForm(forms.Form): # TaskForm is a subclass now of forms.Form
    task_name = forms.CharField()
    task_date = forms.DateField()
    