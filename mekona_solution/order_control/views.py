from django.shortcuts import render
from django.views.generic import View, ListView
from .utils import ObjUpdateMixin, ObjCreateMixin, ObjDeleteMixin
from .models import Order, Task
from .forms import OrderForm, TaskForm
from django.shortcuts import render, redirect, reverse
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.
def mainpage(request):
    return render(request, 'order_control/mainpage.html')

def historypage(request):
    return render(request, 'order_control/history.html')

class OrderCreate(View, ObjCreateMixin):
    model_form = OrderForm
    raise_exeption = True
    template = 'order_control/order_create_form.html'
    def get(self, request, *args, **kwargs):
        form = self.model_form(initial={'order_author': request.user})
        return render(request, self.template, context={'form': form})
    
class OrderUpdate(View, ObjUpdateMixin):
    model_form = OrderForm
    data = Order
    raise_exeption = True
    template = 'order_control/order_update_form.html'

class OrderDelete(View, ObjDeleteMixin):
    raise_exeption = True
    data = Order
    template = 'order_control/order_delete_form.html'

class OrderList(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order_control/orders_list.html'

    def get_queryset(self):
        return Order.objects.all()

def order_detail(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
        context = {'order': order, 'panel': order, 'detail': True}
        # if request.user.is_authenticated:
        #     context['form'] = CommentForm
    except Order.DoesNotExist:
        raise Http404('Заказа не существует!')
    return render(request, 'order_control/order_detail.html', context)

    
