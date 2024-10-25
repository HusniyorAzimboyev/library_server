from django.shortcuts import render, redirect
from .forms import signupform
from .models import upper
from django.http import HttpResponse
def main_page(request):
    form = signupform(request.POST)
    if request.POST and form.is_valid():
        form.save()
        return redirect("table_list")
    context = {"form":form}
    return render(request,"signup.html")

def users_table(request):
    queryset = upper.objects.all()
    html = f"""
        <h1>Hello world</h1>
        <table>
        <tr><th>name</th><th>email</th><th>password</th></tr>
    """
    for i in queryset:
        html+=f"<tr><td>{i.username}</td><td>{i.email}</td><td>{i.password}</td></tr>"
    html+="</table>"
    return HttpResponse(html)