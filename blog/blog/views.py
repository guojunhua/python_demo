from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse


def home(request):
    return HttpResponse('首页')
