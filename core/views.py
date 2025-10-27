from django.shortcuts import render,redirect
from . forms import ProfileForm
from django.http import HttpResponseNotAllowed
from .models import Profile
from django.core.files.storage import default_storage
def index(request):
    #print("view logikasi run boldi")
    return render(request,"core/index.html")


def create_profile(request):
    if request.method == "POST" and request.FILES["image"]:
        form = ProfileForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    return HttpResponseNotAllowed(["POST"])

def profiles(request):
    profiles = Profile.objects.all()
    return render(request,"core/profiles.html",{"profiles":profiles})

def upload_files(request):
    if request.method == "POST" and request.FILES["file"]:
        file = request.FILES['file']
        file_name = default_storage.save(file.name,file)
        file_url = default_storage.url(file_name)
        return render(request,"core/upload-success.html",{"file_url":file_url})
