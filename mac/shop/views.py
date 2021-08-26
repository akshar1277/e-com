
from django.shortcuts import render,redirect
from django.http import HttpResponse
from math import ceil
from .models import Product,Order,OrderUpdate
from django.views import View

# Create your views here.
class Index(View):
    print("**************")


    def post(self,request):
        print("possst")
        product=request.POST.get('product')
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]=quantity -1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1

        request.session['cart']=cart







        print("---------")
        print(product,"jel")
        print(cart)
        value=cart.values()
        total=sum(value)
        print(total)
        return redirect('/shop/')

        # return render(request, 'shop/index.html', total)



    def get(self,request):
        total=0
        cart = request.session.get('cart')
        if cart:

            value = cart.values()
            total = sum(value)
            print(total)
        else:
            request.session['cart']={}
        print("-------get")

        allProds = []
        catprods = Product.objects.values('category', 'id')
        cats = {item['category'] for item in catprods}
        for cat in cats:
            prod = Product.objects.filter(category=cat)
            n = len(prod)
            nSlides = n // 4 + ceil((n / 4) - (n // 4))
            allProds.append([prod, range(1, nSlides), nSlides])

        # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
        # allProds = [[products, range(1, nSlides), nSlides],
        #             [products, range(1, nSlides), nSlides]]
        params = {'allProds': allProds,'total':total}
        return render(request, 'shop/index.html', params)




# def index(request):
#     # products = Product.objects.all()
#     # print(products)
#     # n = len(products)
#     # nSlides = n//4 + ceil((n/4)-(n//4))
#
#     allProds = []
#     catprods = Product.objects.values('category', 'id')
#     cats = {item['category'] for item in catprods}
#     for cat in cats:
#         prod = Product.objects.filter(category=cat)
#         n = len(prod)
#         nSlides = n // 4 + ceil((n / 4) - (n // 4))
#         allProds.append([prod, range(1, nSlides), nSlides])
#
#     # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
#     # allProds = [[products, range(1, nSlides), nSlides],
#     #             [products, range(1, nSlides), nSlides]]
#     params = {'allProds': allProds}
#     return render(request, 'shop/index.html', params)
def about(request):
    return render(request,'shop/about.html')


def contact(request):
    return HttpResponse("we are at contact")

def tracker(request):
    return HttpResponse("we are at tracker")

def search(request):
    return HttpResponse("we are at search")

def productView(request):
    return HttpResponse("we are at productView")

def checkout(request):
    return HttpResponse("we are at checkout")

def cart(request):
    ids=list(request.session.get('cart').keys())
    products=Product.get_products_by_id(ids)
    print(products)
    return render(request,'shop/cart.html',{'products':products})


def checkout(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        car=request.session.get('cart')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '')+ " " + request.POST.get('address2','')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code=request.POST.get('zip_code','')
        phone=request.POST.get('phone','')
        order=Order(name=name,car=car,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone)

        order.save()
        update=OrderUpdate(order_id=order.order_id,update_desc="the order has been placed")
        update.save()
        id=order.order_id
        request.session.get('cart').clear()
        print(request.session.get('cart'))
        thank=True

        return render(request,'shop/thanks.html',{'thank':thank,'id':id})

    elif request.method=="GET":
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        return render(request,'shop/checkout.html',{'products':products})