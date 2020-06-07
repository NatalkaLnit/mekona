from django import forms
from .models import *



class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('order_text', 'type_of_work_fk', 'client_number', 'order_author',  'deadline', )
        widgets = {
            'deadline': forms.DateInput(attrs={'class':'form-control'}),
            # 'order_date_update': forms.SplitDateTimeWidget(attrs={'class':'form-control'}),
            # 'order_date_creation': forms.DateTimeField(attrs={'class':'form-control'}),
            'order_author': forms.HiddenInput(attrs={'class':'form-control'}),
            'order_text': forms.TextInput(attrs={'class':'form-control'}),
            'type_of_work_fk': forms.SelectMultiple(attrs={'class':'form-control'}),
            'client_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'+7(999)-999-99-99'}),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('type_fk', 'order_fk',  'task_executor', 'status','task_author', 'task_text' )
        widgets = {
            'type_fk': forms.Select(attrs={'class':'form-control'}),
            'order_fk': forms.Select(attrs={'class':'form-control'}),
            'task_executor': forms.Select(attrs={'class':'form-control'}),
            'task_author': forms.HiddenInput(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'}),
            'task_text': forms.Textarea(attrs={'class':'form-control'}),
        }
