from django.shortcuts import render
from django.http import HttpResponse

def home_page(self):
    return HttpResponse('<html><title>To-Do Lists</title></html>')