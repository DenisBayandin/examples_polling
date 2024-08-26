from django.urls import path
from .views import short_polling, polling_example


urlpatterns = [
    path('result/', short_polling, name='result'),
    path('polling-example/', polling_example, name='polling_example'),
]
