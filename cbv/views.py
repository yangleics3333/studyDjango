from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.


class NewsView(View):
    def get(requests,self):
        return HttpResponse("get")

    def post(requests,self):
        return HttpResponse("post")
