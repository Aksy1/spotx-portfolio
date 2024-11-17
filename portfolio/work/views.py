from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
def enquiry(request):
    return render(request, 'enquiry.html')
