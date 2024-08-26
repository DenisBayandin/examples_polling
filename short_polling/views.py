from django.http import JsonResponse
from django.shortcuts import render

from .models import Book


def short_polling(request):
    return JsonResponse({'data': list(Book.objects.all().values())})


def polling_example(request):
    return render(request, 'short_polling/example.html')
