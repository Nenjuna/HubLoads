from django.shortcuts import render

from .models import Manga

# Create your views here.
def home_view(request):
    mangas = Manga.objects.all().order_by('updated_at')
    return render(request, 'mangas/pages/home.html', {'mangas': mangas})