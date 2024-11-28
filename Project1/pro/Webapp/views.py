from django.shortcuts import render
from .models import photo
def index(request):
    image = photo.objects.all()
    cloudinary_img={'photo':photo}
    return render(request,"index.html",cloudinary_img)