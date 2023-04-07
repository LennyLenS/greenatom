from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect


def page_not_found_view(request, excaption):
    print("ssssss")
    return HttpResponseNotFound('login')