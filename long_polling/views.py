import time

from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import render

from .models import News


def long_polling(request):
    timeout = 10
    start_time = timezone.now()
    while True:
        new_data = News.objects.all()
        if new_data.count() > 2:
            time.sleep(5)
            return JsonResponse({'data': list(new_data.values())})
        if (timezone.now() - start_time).total_seconds() > timeout:
            return JsonResponse({'data': [{"error": "Timeout!"}]})
        time.sleep(5)


def polling_example(request):
    return render(request, 'long_polling/example.html')
