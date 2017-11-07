from django.shortcuts import render
from .models import Pressure, Weight
from .forms import PostForm


def bphistory(request):
    pressures = Pressure.objects.all().order_by('-date')
    weights = Weight.objects.all().order_by('-date')
    plength = len(pressures)
    return render(request, 'bpmon/bphistory.html', {'pressures': pressures,
                                                    'weights': weights,
                                                    'plength': plength, })


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

    else:
        form = PostForm()
    return render(request, 'bpmon/post_edit.html', {'form': form})
