from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse
import os


# Create your views here.
STRIPE_TEST_SECRET_KEY = os.environ.get('STRIPE_TEST_SECRET_KEY')


class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'


def charge(request):
    amount = 5
    if request.method == 'POST':
        print('Data', request.POST)
    return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
    amount = args
    return render(request, 'orders/success.html', {'amount': amount})
