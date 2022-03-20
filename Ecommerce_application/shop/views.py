from django.shortcuts import HttpResponse, render
from shop.models import Product, Contact, Orders, OrderUpdate
from math import ceil
import json

# Create your views here.
def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds':allProds}
    return render(request, 'shop/index.html',params)


def about(request):
    return render(request, 'shop/AboutUs.html')


def contact(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        desc = request.POST.get("desc","")
        contact = Contact(name = name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'shop/Contact.html',{'thank':thank})


def tracking(request):
    if request.method == "POST":
        orderId = request.POST.get("orderId","")
        email = request.POST.get("email","")
        try:
            order = Orders.objects.filter(order_id = orderId, email=email)
            if len(order)> 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text':item.update_desc, "time": item.timestamp})
                    response  =json.dumps([updates, order[0].item_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')

        except Exception as e:
            return HttpResponse("{}")
    
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/Search.html')


def product_view(request, myid):
    #fetching product from database
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/productView.html', {'product': product[0]})
    

def checkout(request):
    if request.method == "POST":
        item_json = request.POST.get("itemsJson","")
        name = request.POST.get("name","")
        
        email = request.POST.get("email","")
        address = request.POST.get("address1","") + " " + request.POST.get("address2","")
        city = request.POST.get("city","")
        state = request.POST.get("state","")
        zip_code = request.POST.get("zip_code","")
        phone = request.POST.get("phone","")
        
        order = Orders(item_json=item_json, name = name, email=email, address= address, city= city, state= state, zip_code =zip_code, phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="Your orer has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/Checkout.html', {" thank" : thank, "id" : id})
    return render(request, 'shop/Checkout.html')
