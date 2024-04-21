from django.shortcuts import render
from myop.models import User , Film , Role , Review



# Create your views here.
def index_page(request):
    object = Film.objects.all()
    return render(request, 'index.html', context={'object': object})
def user_page(request):
    return render()
def film_page(request):
    return render()

