from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_pages = request.GET.get('sort')
    phone_object = Phone.objects.all()
    if sort_pages == 'min_price':
        phone_object = phone_object.order_by('price')
    elif sort_pages == 'max_price':
        phone_object = phone_object.order_by('-price')
    elif sort_pages == 'name':
        phone_object = phone_object.order_by('name')

    context = {
        'phones': phone_object
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_object = Phone.objects.all()
    cul_phone = ''
    for phone in phone_object:
        if phone.slug == slug:
            cul_phone = phone
    context = {
        'phone': cul_phone
    }
    return render(request, template, context)
