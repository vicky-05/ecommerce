from django.shortcuts import render
from .models import *
from .form import CustomUserForm
from django.contrib import messages
from django.shortcuts import redirect
from .models import productCollection
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
    trend = trend_products.objects.filter(status=0)
    return render(request, "shop/index.html",{'trend':trend})

def logout_page(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect('home')

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:

     if request.method=="POST":
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username=name, password=pwd)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successfully")
            return redirect('home')
        else:
            messages.warning(request, "Invalid Username or Password")
            return redirect('login')
     return render(request, "shop/login.html")

def register(request):
    form=CustomUserForm()
    if request.method=="POST":
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful")
            return redirect('login')
    return render(request, "shop/register.html",{'form':form})
def categories(request):
    category = Category.objects.filter(status=0)
    return render(request, "shop/categories.html",{'category':category})

# def home(request):
#     topBrands = TopBrands.objects.filter(status=0)
#     return render(request, "shop/index.html",{'topBrands':topBrands})

def collections(request):
    return render(request, "shop/products/index.html")

def collectionsview(request,group_name):
    if(Category.objects.filter(product_title=group_name,status=0)):
        productcollection = productCollection.objects.filter(group_name=group_name)
        return render(request, "shop/products/index.html",{'productcollection':productcollection,'group_names':group_name})
    else:
        messages.warning(request, "No such category found")
        return redirect('collections')

def product_details(request, cname, pname):
    if Category.objects.filter(product_title=cname, status=0):
        if productCollection.objects.filter(name_product=pname, status=0):
            products = productCollection.objects.filter(name_product=pname, status=0).first()
            return render(request, "shop/products/products_details.html", {'products': products})
        else:
            messages.warning(request, "No such product found")
            return redirect('collections')

def collections(request):
    # Retrieve distinct brand names
    distinct_brand_names = productCollection.objects.values('brand_name').distinct()

    # Pass the brand names to the template
    return render(request, 'collections.html', {'distinct_brand_names': distinct_brand_names})

def product_detail(request, product_id):
    product = productCollection.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})