from django.shortcuts import render
from .models import Pressure, Weight


def bphistory(request):
    pressures = Pressure.objects.all()
    weights = Weight.objects.all()
    return render(request, 'bpmon/bphistory.html', {'pressures': pressures,
                                                    'weights': weights})
