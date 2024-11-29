
from django.shortcuts import render, redirect
from .models import ServiceRequest

def home(request):
    return render(request, 'main/main.html')

def create_request(request):
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        email = request.POST['email']
        request_type = request.POST['request_type']
        details = request.POST['details']
        
        ServiceRequest.objects.create(
            customer_name=customer_name,
            email=email,
            request_type=request_type,
            details=details
        )
        return redirect('track_requests')
    return render(request, 'main/create_request.html')

def track_requests(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'main/track_requests.html', {'requests': requests})
