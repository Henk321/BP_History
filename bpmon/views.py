from django.shortcuts import render
from .models import Pressure, Weight
from .add_bp import PostBP
from .add_wght import PostWght


def bphistory(request):
    pressures = Pressure.objects.all().order_by('-date')
    weights = Weight.objects.all().order_by('-date')
    plength = len(pressures)
    return render(request, 'bpmon/bphistory.html', {'pressures': pressures,
                                                    'weights': weights,
                                                    'plength': plength, })


def add_blood_pressure(request):
    if request.method == 'POST':
        form = PostBP(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

    else:
        form = PostBP()
    return render(request, 'bpmon/add_bp.html', {'form': form})


def add_weight(request):
    if request.method == 'POST':
        form = PostWght(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

    else:
        form = PostWght()
    return render(request, 'bpmon/add_weight.html', {'form': form})
