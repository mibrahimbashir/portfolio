from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Messages

# Create your views here.

def home(request):
	context = {}
	return render(request, 'index.html', context)

def project_1(request):
	return render(request, 'project-1.html')