from django.shortcuts import render

def index(request, ma_variable):
    return render(request, "template.html", context={'ma_variable': ma_variable})
