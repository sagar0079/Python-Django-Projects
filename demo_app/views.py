# type: ignore
from multiprocessing import context
from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.views.generic import DetailView,CreateView

from .forms import AddItemForm
from .models import FoodList
# Create your views here.

def my_view(request):
    return HttpResponse("<b>this is my view</b>")

def food(request):
    item_list = FoodList.objects.all()
    context = {
        'item_list' : item_list,
    }
    return render(request,'demo_app/food.html',context)

def food_detail(request,item_id):
    item = FoodList.objects.get(pk=item_id)
    context = {
        'item' : item,
    }
    return render(request,'demo_app/food_detail.html',context)

class FoodDetail(DetailView):
    model = FoodList
    template_name = 'demo_app/food_detail.html'
    context_object_name = 'item'
    

def add_item(request):
    form = AddItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('demo_app:food')
    return render(request,'demo_app/add-item.html',{'form':form })

class CreateItem(CreateView):
    model = FoodList
    fields = ['item_name','item_price','item_image','item_desc']
    template_name = 'demo_app/add-item.html'

    def form_valid(self,form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)


def update_item(request,id):
    item = FoodList.objects.get(id = id)
    form = AddItemForm(request.POST or None,instance=item)

    if form.is_valid():
        form.save()
        return redirect('demo_app:food')
    return render(request,'demo_app/add-item.html',{'form':form,'item':item})

def delete_item(request,id):
    item = FoodList.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('demo_app:food')
    return render(request,'demo_app/delete-item.html',{'item':item})