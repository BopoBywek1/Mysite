from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect, get_object_or_404


from myop.forms import RegistrationForm, LoginForm
from myop.models import User , Film , Role , Review





# Create your views here.
def index_page(request):
    search_query = request.GET.get('search_N', '')
    if search_query:
        object = Film.objects.filter(Name_Film=search_query)
    else:
        object = Film.objects.all()
    return render(request, 'index.html', context={'object': object})

def registra_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.ID_Roles = 1
            form.save()
            return redirect('User_page')

    else:
        form = RegistrationForm()
    return render(request, 'Registra.html',{'form': form})
def avtoriz_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            Login = form.cleaned_data['Login']
            login(request, Login)
            return redirect('User_page')
    else:
        form = LoginForm()
    return render(request, 'Avtoriz.html',{'form': form})

def film_page(request, id):
    film = Film.objects.get(ID=id)
    return render(request,"Film.html",{'Film': film})

def user_page(request):
    search_query = request.GET.get('search_N', '')
    if search_query:
        object = Film.objects.filter(Name_Film=search_query)
    else:
        object = Film.objects.all()
    return render(request, 'User.html', context={'object': object})

