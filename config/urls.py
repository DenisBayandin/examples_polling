from django.urls import path, include


urlpatterns = [
    path('short-polling/', include("short_polling.urls")),
    path('long-polling/', include("long_polling.urls")),
    path('events/', include("sse.urls")),
]
