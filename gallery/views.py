from django.shortcuts import render
from .models import GalleryImage

def gallery(request):
    images = GalleryImage.objects.order_by('-uploaded_at')
    return render(request, 'gallery/gallery.html', {'images': images})
