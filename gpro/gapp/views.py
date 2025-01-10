from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .models import Gallery
def main(request):
    gallery_images = Gallery.objects.filter(user=request.user)
    return render(request,'index.html',{"gallery_images": gallery_images})
def login_user(request):
    if "username" in request.session:
        return redirect(main)
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            request.session["username"]=username
            return redirect(main)
        messages.error(request,"wrong password or username")
        return redirect(login_user)
    return render(request,'signin.html')
def signup(request):
    if request.POST:
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        if password == confirmpassword:
            User.objects.create_user(username=username,email=email,password=password)
            return redirect(login_user)
        messages.error(request,"wrong password or username")
        return render(request,'signin.html')
    return render(request,'register.html')
def logout_g(request):
    logout(request)
    request.session.flush()
    return redirect(login_user)
def index(request):
    if request.method == 'POST' and 'image' in request.FILES:  # Ensure the 'image' key is in request.FILES
        myimage = request.FILES['image']  # Access the uploaded image from request.FILES
        obj = Gallery(feedimage=myimage,user=request.user)  # Create an instance of Gallery and save the image
        obj.save()  # Save the object to the database
        return redirect('image')  # Redirect back to the index page after saving
    # Retrieve all gallery images to display
    return render(request, "add.html")

def delete_g(request,id):
    feeds=Gallery.objects.filter(pk=id)
    feeds.delete()
    return redirect(index)
def add(request):
     return render(request,"add.html")
def register(request):
     return render(request,"register.html")
# Create your views here.





