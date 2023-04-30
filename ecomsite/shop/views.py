from django.shortcuts import render,redirect
from .models import product,order
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    obj=product.objects.all()

    item_name=request.GET.get('item-search',None)
    print(item_name)

    #search code
    if item_name:
        obj =obj.filter(name__icontains=item_name)
            
    #paginator code
    paginator=Paginator(obj,4)
    page=request.GET.get('page')
    obj=paginator.get_page(page)

    return render(request,'shop/index.html',{'obj':obj})


def details(request,id):
    product_obj=product.objects.get(id=id)
    return render(request,'shop/detail.html',{'product':product_obj})


def checkout(request):
    if request.method=="POST":
        item=request.POST.get("item")
        name=request.POST.get("name")
        city=request.POST.get("city")
        zipcode=request.POST.get("zip")
        state=request.POST.get("state")
        address=request.POST.get("address")
        email=request.POST.get("email")

        order1=order(item=item, name=name,city=city,zipcode=zipcode,state=state,address=address,email=email)
        order1.save()


    
    return render(request,'shop/checkout.html',)