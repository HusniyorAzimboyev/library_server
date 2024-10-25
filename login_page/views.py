from django.shortcuts import render
from .models import user

def log_in(request):
    if request.method == "POST":
        model = user()
        model.name = request.POST.get("username",'')
        model.password = request.POST.get('password','')
        model.save()
        print(request.POST)
    return render(request,'login.html')
def new_page(request):
    return render(request,'login.html')