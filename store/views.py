from django.shortcuts import redirect, render, get_object_or_404

from store.forms import CategoryForm, ProductForm, OrderForm
from store.models import Category, Product, Order


def createcategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store:readcategory')
    else:
        form = CategoryForm
    return render(request, "createcategory.html", {'form': form})


def readcategory(request):
    category = Category.objects.all()
    context = {
        'category': category
    }
    return render(request, 'readcategory.html', context)


def updatecategory(request, id):
    updateitem = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=updateitem)
        if form.is_valid():
            form.save()
            return redirect('store:readcategory')
    else:
        form = CategoryForm(instance=updateitem)
    return render(request, 'updatecategory.html', {'form': form})


def deletecategory(request, id):
    deleteitem = get_object_or_404(Category, id=id)
    deleteitem.delete()
    return redirect('store:readcategory')


def createproduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store:readproduct')
    else:
        form = ProductForm
    return render(request, "createproduct.html", {'form': form})


def readproduct(request):
    product = Product.objects.all()
    context = {
        'product': product
    }
    return render(request, 'readproduct.html', context)


def updateproduct(request, id):
    updateitem = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=updateitem)
        if form.is_valid():
            form.save()
            return redirect('store:readproduct')
    else:
        form = ProductForm(instance=updateitem)
    return render(request, 'updateproduct.html', {'form': form})


def deleteproduct(request, id):
    deleteitem = get_object_or_404(Product, id=id)
    deleteitem.delete()
    return redirect('store:readproduct')


def createorder(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store:readorder')
    else:
        form = OrderForm
    return render(request, "createorder.html", {'form': form})


def readorder(request):
    order = Order.objects.all()
    context = {
        'order': order
    }
    return render(request, 'readorder.html', context)


def updateorder(request, id):
    updateitem = get_object_or_404(Order, id=id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=updateitem)
        if form.is_valid():
            form.save()
            return redirect('store:readorder')
    else:
        form = OrderForm(instance=updateitem)
    return render(request, 'updateorder.html', {'form': form})


def deleteorder(request, id):
    deleteitem = get_object_or_404(Order, id=id)
    deleteitem.delete()
    return redirect('store:readorder')
