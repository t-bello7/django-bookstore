from django.urls import path
from .views import OrdersPageView, charge, successMsg

urlpatterns = [
    path('', OrdersPageView.as_view(), name='orders'),
    path('charge/', charge, name='charge'),
    path('succes/<str:args>/', successMsg, name="success"),
]
