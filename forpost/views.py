from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Lone, Payback


def PaybackAjax(request, pk):
    object = get_object_or_404(Payback, pk=pk)

    data = {
        'id'          : object.id,
        'lone_id'     : object.lone_id.id,
        'payback'     : object.payback,
    }
    return JsonResponse(data)


def LoneListView(request):
    template = 'lone_list.html'
    Lone_data = Lone.objects.all()
    Payback_data = Payback.objects.values_list('id')
    Payback_id = []
    for i in Payback_data:
        Payback_id.append(i[0])

    return render(request, template, {
        'Lone_data': Lone_data,
        'Payback_id': Payback_id,
    })