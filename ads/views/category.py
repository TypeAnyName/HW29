import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from ads.models import Category


@method_decorator(csrf_exempt, name="dispatch")
class CategoryListView(ListView):
    model = Category
    queryset = Category.objects.all()

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object_list = self.object_list.order_by('name')

        return JsonResponse(data=[
            {"id": cat.id,
             "name": cat.name,
             }
            for cat in self.object_list
        ], safe=False, json_dumps_params={"ensure_ascii": False})


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        cat = self.get_object()
        return JsonResponse({'id': cat.id, "name": cat.name}, safe=False,
                            json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class CategoryCreateView(CreateView):
    model = Category
    fields = ('name',)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        new_category = Category.objects.create(name=data['name'])
        return JsonResponse({'id': new_category.id, "name": new_category.name}, safe=False,
                            json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ("name",)

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        data = json.loads(request.body)
        self.object.name = data['name']
        self.object.save()

        return JsonResponse({'id': self.object.id, "name": self.object.name}, safe=False,
                            json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({}, status=204)
