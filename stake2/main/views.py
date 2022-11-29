from django.shortcuts import render

# Create your views here.


def reg(request):
    context = {}
    return render(request, 'main/reg.html', context)


def money(request):
    context = {}
    return render(request, 'main/money.html', context)