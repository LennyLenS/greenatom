from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect


def page_405(request, a):
    print("Fdfdfd")
    return redirect('login')


def page_404(request):
    return redirect('login')

