from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name = 'mainpage_url'),
    path('history/', views.historypage, name = 'history_url'),
    path('order_create/', views.OrderCreate.as_view(), name = 'order_create_url'),
    path('orders_list/', views.OrderList.as_view(), name = 'orders_list_url'),
    path('orders/<int:order_id>', views.order_detail, name="order_detail_url"),
    path('orders/<int:obj_id>/order_update/',
         views.OrderUpdate.as_view(), name="order_update_url"),
    path('orders/<int:obj_id>/order_delete/',
         views.OrderDelete.as_view(), name="order_delete_url"),
]
