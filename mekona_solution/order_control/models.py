from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Type_of_work(models.Model):
    name_of_type = models.CharField(max_length = 200, 
                                    verbose_name = 'Виды работ')
    class Meta:
        verbose_name = 'Вид работы'
        verbose_name_plural = 'Виды работ'

    def __str__(self):
        return self.name_of_type

class Profile(models.Model):
    # CASCADE means if the user is deleted the profile is deleted
    # However, If the profile is deleted, the user is not deleted.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"user_id": self.user.pk})
    
    def get_update_url(self):
        return reverse("profile_update_url", kwargs={"user_id": self.user.pk})


class Order(models.Model):
    order_author = models.ForeignKey(User, on_delete=models.CASCADE,
                                    verbose_name = 'Автор' )
    order_text = models.TextField(verbose_name = 'Текст')
    order_date_creation = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата создания')
    order_date_update = models.DateTimeField(auto_now=True,
                                    verbose_name='Дата изменения', 
                                    blank=True, null=True)
    type_of_work_fk = models.ManyToManyField(Type_of_work, through = 'Order_Type', 
                                    verbose_name = 'Виды работ')
    client_number = PhoneNumberField(verbose_name = 'Номер обратной связи') #  +7(222)-222-23-23
    deadline = models.DateField(blank=True, null=True, 
                                    verbose_name= 'Дата окончания')
                    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
    
    def __str__(self):
        return '{} {} | {}'.format(self.order_author.first_name, self.order_author.last_name,  self.order_date_creation)
    
    def get_absolute_url(self):
        return reverse("order_detail_url", kwargs={"order_id": self.pk})
    
    def get_update_url(self):
        return reverse("order_update_url", kwargs={"obj_id": self.pk})

    def get_delete_url(self):
        return reverse("order_delete_url", kwargs={"obj_id": self.pk})

class Order_Type(models.Model):
    type_fk = models.ForeignKey(Type_of_work, on_delete=models.CASCADE)
    order_fk = models.ForeignKey(Order, on_delete=models.CASCADE)
    count = models.FloatField(verbose_name = 'Стоимость', blank=True, null=True)

    class Meta:
        verbose_name = 'Вид работ в заказе'
        verbose_name_plural = 'Виды работ в заказе'

class Task(models.Model):
    type_fk = models.ForeignKey(Type_of_work, verbose_name = 'Тип работ',
                                blank=True, null=True, 
                                on_delete=models.SET_NULL)
    order_fk = models.ForeignKey(Order, verbose_name = 'Заказ', blank=True,
                                null=True, on_delete=models.SET_NULL)
    task_author = models.ForeignKey(User, on_delete=models.CASCADE,
                                verbose_name = 'Отвественный', related_name= '+' )
    task_executor  = models.ForeignKey(User, on_delete=models.SET_NULL,
                                verbose_name = 'Исполнитель', blank=True, null=True, related_name = '+')

    TASK_STATUS = (
        ('L', 'Принята в обработку'),
        ('С', 'Выполнена'),
        ('F', 'Отменена'),
    )

    status = models.CharField(max_length=1, choices=TASK_STATUS,
                                default='L', verbose_name = 'Cтатус',
                                help_text='Статус задачи')   

    
    task_text = models.CharField(max_length=250, verbose_name = 'Описание задачи')
    task_date_creation = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата создания')
    task_date_comleate = models.DateTimeField(verbose_name='Дата завершения', 
                                    blank=True, null=True)
                            
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задача'
        

    def __str__(self):
        return 'Отвественный: {}, Исполнитель: {}'.format(self.task_author, self.task_executor)

    def get_absolute_url(self):
        return reverse("task_detail_url", kwargs={"task_id": self.pk})
    
    def get_update_url(self):
        return reverse("task_update_url", kwargs={"obj_id": self.pk})

    def get_delete_url(self):
        return reverse("task_delete_url", kwargs={"obj_id": self.pk})

from django.contrib.auth.models import User

def get_user_name(self):
    return '{} {} | {}'.format(self.first_name, self.last_name, self.username)

User.add_to_class("__str__", get_user_name)