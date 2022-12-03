from django.shortcuts import render

# Create your views here.
def boot_cdn(requset):
    return render(requset,'boot_cdn.html')