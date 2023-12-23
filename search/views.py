from django.shortcuts import render
from .models import Post
from django.db.models import Q

def index(request):
    if 'qidirish' in request.GET:
        search = request.GET['qidirish']
        q = Q(Q(ism__icontains=search) | Q(fam__icontains=search) | Q(yosh__icontains=search) | Q(adres__icontains=search))
        posts = Post.objects.filter(q)
    else:
        posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'index.html', context)

