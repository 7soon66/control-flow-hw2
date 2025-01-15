from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Donkey,Toy
# we use .edit because we are updating it in our DB
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView 
from .forms import FeedingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class DonkeyCreate(LoginRequiredMixin,CreateView):
    model = Donkey
    # feilds = all in our model that we want them to be entered
    fields = ["name","breed","describtion","age","image"]
    # success_url='/cats/' #it laed us to the cats page if it was created sucsessfuly
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class DonkeyUpdate(LoginRequiredMixin,UpdateView):
    model=Donkey
    fields=["name","breed","describtion"]

class DonkeyDelete(LoginRequiredMixin,DeleteView):
    model=Donkey
    success_url='/donkeys/'

class ToyList(LoginRequiredMixin,ListView):
    model=Toy

class ToyDetail(LoginRequiredMixin,DetailView):
    model=Toy

class ToyCreate(LoginRequiredMixin,CreateView):
    model=Toy
    fields="__all__"
class ToyUpdate(LoginRequiredMixin,UpdateView):
    model=Toy
    fields=['name','color']

class ToyDelete(LoginRequiredMixin,DeleteView):
    model=Toy
    success_url="/toys/"
# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')

@login_required
def donkey_index(request):
    # Select * from main_app_cat
    # donkeys=Donkey.objects.all()
    donkeys = Donkey.objects.filter(user = request.user)
    return render(request, 'donkeys/index.html', {'donkeys':donkeys})
@login_required
def donkey_detail(request, donkey_id):
  donkey = Donkey.objects.get(id=donkey_id)
  feeding_form= FeedingForm()
  #Exl
  toys_donkey_dosent_have=Toy.objects.exclude(id__in=donkey.toys.all().values_list('id'))
  return render(request, 'donkeys/detail.html', {'donkey': donkey, 'feeding_form':feeding_form,"toys":toys_donkey_dosent_have})
@login_required
def add_feeding(request,donkey_id):
    form=FeedingForm(request.POST)
    if form.is_valid():
        new_feeding=form.save(commit=False)
        new_feeding.donkey_id=donkey_id
        new_feeding.save()
    return redirect('detail', donkey_id = donkey_id)
@login_required
def assoc_toy(request,donkey_id,toy_id):
    Donkey.objects.get(id=donkey_id).toys.add(toy_id)
    return redirect('detail',donkey_id=donkey_id)
@login_required
def unassoc_toy(request,donkey_id,toy_id):
    Donkey.objects.get(id=donkey_id).toys.remove(toy_id)
    return redirect('detail',donkey_id=donkey_id)

def signup(request):
    error_message=''
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("index")
        else:
            error_message='invalid Signup- please try again later.'
        
    form=UserCreationForm()
    context={"form":form,'error_message':error_message}
    return render(request, 'registration/signup.html',context)