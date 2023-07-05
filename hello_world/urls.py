from django.urls import path

from hello_world.views import HelloWorld

urlpatterns = [
    path('hello-world/', HelloWorld.as_view())
]