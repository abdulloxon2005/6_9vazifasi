from django.shortcuts import render


def index(request):
    #print("view logikasi run boldi")
    return render(request,"core/index.html")