from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect

from .forms import NewItemForm, EditItemForm

from .models import Category,Item


def items(request):
    query = request.GET.get('query', '')
    category_id =request.GET.get('category','')
    categories=Category.objects.all()
    items = Item.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    
    if category_id:
        items = items.filter(category_id=category_id)

    # Check if there are no items in the specified category
    no_items_in_category = not items.exists()


    return render(request, 'item/items.html', {'items': items, 'query': query, 'categories': categories,'category_id': category_id,'no_items_in_category': no_items_in_category, })

    

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    relate_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    
    return render(request, 'item/detail.html',{
        'item':item,
        'relate_items': relate_items,
        
        
        
    })

@login_required 
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return render(request, 'item/detail.html', {'item': item})
    else:
        form = NewItemForm()
    
    return render(request, 'item/form.html', {'form': form, 'title': 'New item'})

@login_required
def delete(request,pk):
    item= get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard:index')
    

@login_required 
def edit(request, pk):
    item= get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=pk)
    else:
        form = EditItemForm(instance=item)
    
    return render(request, 'item/form.html', {'form': form, 'title': 'Edit item'})

@login_required
def delete(request,pk):
    item= get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard:index')
    

#New views for showing iteam

