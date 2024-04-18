from django.shortcuts import render
from myop.models import Users , Films


# Create your views here.
def index_page(request):
    object = Films.objects.all()
    return render(request, 'index.html', context={'object': object})
