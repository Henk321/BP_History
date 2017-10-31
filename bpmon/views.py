from django.shortcuts import render

def bphistory(request):
    return render(request, 'bpmon/bphistory.html')
