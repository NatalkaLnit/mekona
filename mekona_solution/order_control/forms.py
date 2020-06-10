from django import forms
from .models import *
from django.contrib.auth.models import User



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
    task_executor = forms.ModelChoiceField(queryset=User.objects.all().exclude(is_staff = False), widget=forms.Select(attrs={'class':'form-control'}), label='Исполнитель')
    cost = forms.FloatField()
    class Meta:
        model = Task
        fields = ('order_fk', 'type_fk',   'task_executor', 'status','task_author', 'task_text' )
        widgets = {
            'type_fk': forms.Select(attrs={'class':'form-control'}),
            'order_fk': forms.Select(attrs={'class':'form-control'}),
            
            'task_author': forms.HiddenInput(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'}),
            'task_text': forms.Textarea(attrs={'class':'form-control'}),
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']
        widgets = {
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control', 'readonly':''}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
        }
