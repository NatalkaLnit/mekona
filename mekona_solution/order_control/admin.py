from django.contrib import admin
from .models import *

admin.site.register(Type_of_work)

class OrderTypeInline(admin.TabularInline):
    '''Tabular Inline View for OrderType'''

    model = Order_Type
    extra = 0
    

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ('order_author', 'order_text', 'client_number', )
    list_display = ('order_author', 'order_text', 'order_date_creation', 'order_date_update', 'client_number', 'deadline' )
    list_filter = ('order_author', 'order_date_creation')
    inlines = (OrderTypeInline,)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('type_fk', 'order_fk', 'task_author', 'task_executor', 'status', 'task_text', 'task_date_creation', 'task_date_comleate', )
    list_filter = ('task_author', 'task_date_creation')

