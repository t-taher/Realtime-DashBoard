from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/dash/', consumers.DashConsumer),
    re_path(r'ws/add/', consumers.AddConsumer),

]
