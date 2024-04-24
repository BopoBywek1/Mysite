from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from myop.models import User , Film , Role , Review
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# Create your views here.
def index_page(request):
    search_query = request.GET.get('search_N', '')
    if search_query:
        object = Film.objects.filter(Name_Film=search_query)
    else:
        object = Film.objects.all()
    return render(request, 'index.html', context={'object': object})
def registra_page(request):
    return render(request, 'Registra.html')
def avtoriz_page(request):
    return render(request,'Avtoriz.html')
def film_page(request, ID):
    post = get_object_or_404(Film, pk=ID)
    return render(request,"Film.html",{'film':Film})
