from django.shortcuts import render

# Create your views here.
def pag(request):
    return render(request,'index.html')