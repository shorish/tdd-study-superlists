from django.shortcuts import render, redirect
# from django.http import HttpResponse
from lists.models import Item

# Create your views here.
# home_page = None


def home_page(request):
    # return HttpResponse('<html><title>To-Do lists</title></html>')
    # if request.method == "POST":
    #     return HttpResponse(request.POST['item_text'])
    # return render(request, 'home.html')

    # item = Item()
    # item.text = request.POST.get('item_text', '')
    # item.save()

    if request.method == 'POST':
        Item.objects.create(text=request.POST.get('item_text'))
        return redirect('/lists/the-only-list-in-the-world/')

    # items = Item.objects.all()

    # return render(request, 'home.html',
    #               {'new_item_text': new_item_text,
    #                })
    # return render(request, 'home.html', {'items': items})
    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
