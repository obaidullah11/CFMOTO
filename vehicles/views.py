from django.shortcuts import render
from vehicles.models import *
from django.http import JsonResponse
# Create your views here.
def get_attributes(request):
    category_id = request.GET.get('category_id')
    data = {
        'ModelName': list(ModelName.objects.filter(category=category_id).values('id', 'name')),
        'Factory_name': list(Factory.objects.filter(category=category_id).values('id', 'name')),
        'EUTypeApproval': list(EUTypeApproval.objects.filter(category=category_id).values('id', 'name')),
        'SteeringPower': list(SteeringPower.objects.filter(category=category_id).values('id', 'name')),
        'Wheels': list(Wheels.objects.filter(category=category_id).values('id', 'name')),
        'Color': list(Color.objects.filter(category=category_id).values('id', 'name')),
        'Screen': list(Screen.objects.filter(category=category_id).values('id', 'name')),
        'CargoCompartment': list(CargoCompartment.objects.filter(category=category_id).values('id', 'name')),
        'CommunicationTerminal': list(CommunicationTerminal.objects.filter(category=category_id).values('id', 'name')),
        'SKU': list(SKU.objects.filter(category=category_id).values('id', 'name')),
    }
    return JsonResponse(data)
