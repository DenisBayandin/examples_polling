from django.urls import path
from .views import sse_result, sse_example


urlpatterns = [
    path('result/', sse_result, name='result'),
    path('sse-example/', sse_example, name='sse-example'),
]
