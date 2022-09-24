import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from ads.models import Category, Ad


def index(request):
    return JsonResponse({"status": "ok"})


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


@method_decorator(csrf_exempt, name="dispatch")
class AdsView(View):
    def get(self, request):
        ads = Ad.objects.all()

        res = []
        for ad in ads:
            res.append({"id": ad.id,
                        "name": ad.name,
                        "author": ad.author,
                        "price": ad.price,
                        "description": ad.description,
                        "address": ad.address,
                        "is_published": ad.is_published})

        return JsonResponse(res, safe=False, json_dumps_params={"ensure_ascii": False})

    def post(self, request):
        data = json.loads(request.body)
        new_ad = Ad.objects.create(name=data['name'],
                                   author=data['author'],
                                   price=data['price'],
                                   description=data['description'],
                                   address=data["address"],
                                   is_published=data["is_published"])
        return JsonResponse({"id": new_ad.id,
                             "name": new_ad.name,
                             "author": new_ad.author,
                             "price": new_ad.price,
                             "description": new_ad.description,
                             "address": new_ad.address,
                             "is_published": new_ad.is_published}, safe=False,
                            json_dumps_params={"ensure_ascii": False})


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse({"id": ad.id,
                             "name": ad.name,
                             "author": ad.author,
                             "price": ad.price,
                             "description": ad.description,
                             "address": ad.address,
                             "is_published": ad.is_published}, safe=False,
                            json_dumps_params={"ensure_ascii": False})
