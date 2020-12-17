from django.http import JsonResponse
from django.shortcuts import render
# from dashboard.models import Order
from portfolio.models import Project
from django.core import serializers


# # Create your views here.
# def dashboard_with_pivot(request):
#     return render(request, 'dashboard_with_pivot.html', {})


# def pivot_data(request):
#     dataset = Order.objects.all()
#     data = serializers.serialize('json', dataset)
#     return JsonResponse(data, safe=False)

    ###############################################################################################
# Create your views here.
def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})


def pivot_data(request):
    dataset = Project.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)