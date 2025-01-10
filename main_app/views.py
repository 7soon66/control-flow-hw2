from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Donkey
from django.views.generic.edit import CreateView,UpdateView,DeleteView 
from .forms import FeedingForm

class DonkeyCreate(CreateView):
    model = Donkey
    # feilds = all in our model that we want them to be entered
    fields = ["name","breed","describtion","age","image"]
    # success_url='/cats/' #it laed us to the cats page if it was created sucsessfuly

class DonkeyUpdate(UpdateView):
    model=Donkey
    fields=["name","breed","describtion"]

class DonkeyDelete(DeleteView):
    model=Donkey
    success_url='/donkeys/'

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello Donkey Collector</h1>')
def about(request):
    return render(request, 'about.html')


def donkey_index(request):
    # Select * from main_app_cat
    donkeys=Donkey.objects.all()
    return render(request, 'donkeys/index.html', {'donkeys':donkeys})

def donkey_detail(request, donkey_id):
  donkey = Donkey.objects.get(id=donkey_id)
  feeding_form= FeedingForm()
  return render(request, 'donkeys/detail.html', {'donkey': donkey, 'feeding_form':feeding_form})

def add_feeding(request,donkey_id):
    form=FeedingForm(request.POST)
    if form.is_valid():
        new_feeding=form.save(commit=False)
        new_feeding.donkey_id=donkey_id
        new_feeding.save()
    return redirect('detail', donkey_id = donkey_id)