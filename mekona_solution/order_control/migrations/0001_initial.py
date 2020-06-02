# Generated by Django 3.0.6 on 2020-06-01 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_text', models.TextField(verbose_name='Текст')),
                ('order_date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('order_date_update', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('client_number', models.CharField(max_length=17, verbose_name='Номер обратной связи')),
                ('deadline', models.DateField(blank=True, null=True, verbose_name='Дата окончания')),
                ('order_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Type_of_work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_type', models.CharField(max_length=200, verbose_name='Виды работ')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('L', 'Принята в обработку'), ('С', 'Выполнена'), ('F', 'Отменена')], default='L', help_text='Статус задачи', max_length=1, verbose_name='Cтатус')),
                ('task_text', models.CharField(max_length=250, verbose_name='Описание задачи')),
                ('task_date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('task_date_comleate', models.DateTimeField(blank=True, null=True, verbose_name='Дата завершения')),
                ('order_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order_control.Order', verbose_name='Заказ')),
                ('task_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Отвественный')),
                ('task_executor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель')),
                ('type_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order_control.Type_of_work', verbose_name='Тип работ')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задача',
            },
        ),
        migrations.CreateModel(
            name='Order_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.FloatField(verbose_name='Стоимость')),
                ('order_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_control.Order')),
                ('type_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_control.Type_of_work')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='type_of_work_fk',
            field=models.ManyToManyField(through='order_control.Order_Type', to='order_control.Type_of_work', verbose_name='Виды работ'),
        ),
    ]