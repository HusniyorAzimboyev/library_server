from django.shortcuts import render
from library.models import Author,Book,Genre

def main(request):
    author = Author.objects.all().order_by("name")
    return render(request,'index.html',{"authors":author})