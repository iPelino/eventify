from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets

from api.serializers import CategorySerializer
from events.models import Category


# Create your views here.
def event_list(request):
    return None


# def category_list(request):
#     if request.method == 'GET':
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return JsonResponse(serializer.data, safe=False)
#

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer