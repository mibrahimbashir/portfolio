from django.shortcuts import redirect, render
from .models import Messages
import re

# Create your views here.

def validate_email(email):
    # Define the regex pattern for email
    pattern = r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$"
    
    # Use re.match to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

def home(request):      
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		message = request.POST.get('message')

		Messages.objects.create(name=name, email=email, message=message)
		return redirect('thank-you')

	return render(request, 'index.html')

def project_1(request):
	return render(request, 'project-1.html')

def contact_success(request):
	return render(request, 'thank-you-page.html')