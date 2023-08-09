from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
#import django decorators
from django.contrib.auth.decorators import login_required

#here we are importing models
from .models import *


#importing the model forms like Addform, saleform
from .forms import *

#importing filters
from .filters import *

def home(request):
#here we're querying being ordered by id
    products = Product.objects.all().order_by('-id')
    product_filters = ProductFilter(request.GET,queryset = products)
#Query set
    products = product_filters.qs 
    return render(request,'spare/home.html', {'products': products, 'product_filters': product_filters})


def index(request):
    return render(request, 'spare/index.html')
# Create your views here.

def home2(request):
    return render(request, 'spare/home2.html')

#home page views
@login_required
def product_detail(request, product_id):
    product = Product.objects.get(id = product_id)
    return render(request,'spare/product_detail.html',{'product': product})

#Reciept url views
@login_required
def receipt(request):
    sales = Sale.objects.all().order_by('-id')
    return render(request,'spare/receipt.html',{'sales': sales})


def receipt_detail(request, receipt_id):
    receipt = Sale.objects.get(id = receipt_id)
    return render(request, 'spare/receipt_detail.html', {'receipt': receipt})

#All sales made views
def all_sales(request):
    sales = Sale.objects.all()
    total = sum([items.amount_received for items in sales])
    change = sum([items.get_change() for items in sales])
    net = total - change
    return render(request, 'spare/all_sales.html', {'sales':sales, 'total':total, 'change':change, 'net':net})

@login_required
def issue_item(request,pk):
    issued_item = Product.objects.get(id = pk)
    sales_form = SaleForm(request.POST)
    
    if request.method == 'POST':
        if sales_form.is_valid():
            new_sale = sales_form.save(commit= False)
            new_sale.item = issued_item
            new_sale.unit_price = issued_item.unit_price
            new_sale.save()
            #keeping track of the stock remaining after the sale
            issued_quantity = int(request.POST['quantity'])
            issued_item.total_quantity -= issued_quantity
            issued_item.save()
            
            print(issued_item.item_name)
            print(request.POST['quantity'])
            print(issued_item.total_quantity)
            
            return redirect('receipt')
    return render(request,'spare/issue_item.html',{'sales_form': sales_form})    


#Add to stock views
@login_required
def add_to_stock(request, pk):
    issued_item = Product.objects.get(id=pk)
    form = AddForm(request.POST)
    
    if request.method=='POST':
        if form.is_valid():
            added_quantity = int(request.POST['received_quantity'])
            issued_item.total_quantity += added_quantity
            issued_item.save()
            #to add to the remaining stock quantity is reduced
            print(added_quantity)
            print(issued_item.total_quantity)
            return redirect('home')
    return render(request,'spare/add_to_stock.html',{'form':form})

#this view is for user registration
def register(request):
    #this get method gets the entered data on the form
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'spare/register.html', {'form': form})
    #This method posts the data entered into the form
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            #This redirects to the login page
            return redirect('login')
        else:
            #This incase the login fails the user stays on the register page
            return render(request, 'spare/register.html', {'form':form})

#delete function view
@login_required
def delete_product(request, product_id):
    delete_product = Product.objects.get(id=product_id)
    delete_product.delete()
    return HttpResponseRedirect(reverse('home'))