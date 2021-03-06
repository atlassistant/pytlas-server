from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@login_required(login_url='/admin')
def index(request):
  return render(request, 'index.html')

@api_view()
def api_index(request):
  return Response({
    'first_name': 'John',
    'last_name': 'Doe',
  })