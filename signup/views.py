from django.shortcuts import render, redirect
from .forms import signupform
from .models import upper,just_log
from django.http import HttpResponse
def main_page(request):
    form = signupform(request.POST)

    if request.POST and form.is_valid():
        form.save()
        return redirect("table_list")
    context = {"form":form}
    return render(request,"just_log.html")

def users_table(request):
    queryset = just_log.objects.all()
    html = f"""
        <h1>Hello world</h1>
        <table border=3>
        <tr><th>№</th><th style="border-color:red;border-width:medium;">name</th><th style="border-color:blue;border-width:medium;">email</th><th style="border-color:orange;border-width:medium;">password</th></tr>
    """
    for i in queryset:
        html+=f"<tr><td>{i.id}</td><td>{i.name}</td><td>{i.surname}</td><td>{i.age}</td></tr>"
    html += "</table>"
    return HttpResponse(html)