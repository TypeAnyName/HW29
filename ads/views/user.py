import json

from django.conf import settings
from django.core.paginator import Paginator
from django.db.models import Count
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from ads.models import User
from ads.serializers import *


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserViewSet(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


@method_decorator(csrf_exempt, name="dispatch")
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', "last_name", "username", "role", "age")

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        user_data = json.loads(request.body)
        self.object.first_name = user_data['first_name']
        self.object.last_name = user_data["last_name"]
        self.object.username = user_data['username'],
        self.object.role = user_data["role"],
        self.object.age = user_data["age"],

        self.object.save()

        return JsonResponse({"id": self.object.id,
                             "first_name": self.object.first_name,
                             'last_name': self.object.last_name,
                             'username': self.object.username,
                             "role": self.object.role,
                             "age": self.object.age,
                             }, safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class UserDeleteView(DeleteView):
    model = User
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({}, status=204)
