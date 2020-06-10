from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name = 'mainpage_url'),
    path('history/', views.historypage, name = 'history_url'),
    
    path('order_list/', views.OrderList.as_view(), name = 'order_list_url'),
    path('order/<int:order_id>', views.order_detail, name="order_detail_url"),
    path('order_create/', views.OrderCreate.as_view(), name = 'order_create_url'),
    path('order/<int:obj_id>/order_update/', views.OrderUpdate.as_view(), name="order_update_url"),
    path('order/<int:obj_id>/order_delete/', views.OrderDelete.as_view(), name="order_delete_url"),
    #path('order/<int:order_id>/order_pdf/', views.html_to_pdf_view, name="order_pdf_url"),
    
    
    path('task_list/', views.TaskList.as_view(), name = 'task_list_url'),
    path('task/<int:task_id>', views.task_detail, name="task_detail_url"),
    path('task_create/', views.TaskCreate.as_view(), name = 'task_create_url'),
    path('task/<int:obj_id>/task_update/', views.TaskUpdate.as_view(), name="task_update_url"),
    path('task/<int:obj_id>/task_delete/',  views.TaskDelete.as_view(), name="task_delete_url"),
    
    path('account/', views.UserUpdateView.as_view(), name="profile_detail_url"),
    path('account/update', views.UserUpdateView.as_view(), name="profile_update_url"),
    path('account/orders', views.ClientOrderListView.as_view(), name="user_orders_detail_url"),
    path('account/tasks_worker', views.WorkerTaskListView.as_view(), name="worker_tasks_url"),
    path('account/tasks_admin', views.AdminTaskListView.as_view(), name="admin_tasks_url"),
]
