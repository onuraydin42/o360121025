from django.shortcuts import render
from django.http import HttpResponse

def home(request):
 return render(request, 'index.html')
def about(request):
 return HttpResponse('<h1>Welcome to About Page</h1>')
def signin(request):
 email = request.GET.get('email')
 return render(request, 'signin.html', {'email':email})
def base(request):
 return render(request, 'base.html')