from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    html = """<h1>Welcome To Husniyor's django app!</h1>
        <ul>
            <a href="../library"><li>Library</li></a>
            <a href='../new'><li>Devices</li></a>
            <a href='../signup'><li>Sign up</li></a>
            <a href='../login'><li>Log in</li></a>
        </ul>
        """
    return HttpResponse(html)