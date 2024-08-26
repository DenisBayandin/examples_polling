from django.urls import path
from .views import long_polling, polling_example


urlpatterns = [
    path('result/', long_polling, name='result'),
    path('polling-example/', polling_example, name='polling_example'),
]
