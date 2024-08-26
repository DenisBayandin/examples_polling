from django.shortcuts import render

from django.http import StreamingHttpResponse
from datetime import datetime

import time


def sse_result(request):
    def event_stream():
        while True:
            time.sleep(10)
            yield 'data: Current time: %s\n\n' % datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')


def sse_example(request):
    return render(request, 'sse/example.html')


"""
Установка соединения: Клиент (браузер) открывает соединение с сервером с помощью EventSource.

Поддержка соединения: После установки соединения сервер продолжает отправлять данные через это соединение. В идеале соединение должно оставаться открытым, пока не будет закрыто клиентом или сервером.

Статус ответа: Когда клиент делает запрос на EventSource, сервер отвечает с кодом 200 OK, чтобы подтвердить установление соединения. Это стандартный HTTP-статус для успешного выполнения запроса. Этот статус кода возвращается один раз при установлении соединения и не меняется, пока соединение открыто.

Передача данных: Данные передаются через это же соединение в формате SSE (например, data: <данные>\n\n). Сервер поддерживает соединение открытым, а не закрывает его сразу после отправки данных.
"""
