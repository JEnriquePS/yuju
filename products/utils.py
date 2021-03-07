import json

from django.conf import settings


def get_headers():
    headers = {'Content-Type': 'application/json',
               'Authorization': settings.TOKEN_APP}
    return headers


def get_data_product_simple(form):
    images_urls = []
    if form.cleaned_data['image01'] != '':
        images_urls.append({'url': form.cleaned_data['image01']})
    try:
        if form.cleaned_data['image02'] != '':
            images_urls.append({'url': form.cleaned_data['image02']})
    except Exception:
        pass

    data = {
        "price": form.cleaned_data['price'],
        "sku": form.cleaned_data['sku'],
        "stock": form.cleaned_data['stock'],
        "name": form.cleaned_data['name'],
        "brand": form.cleaned_data['brand'],
        "description": form.cleaned_data['description'],
        "dimensions_unit": form.cleaned_data['dimensions_unit'],
        "shipping_depth": form.cleaned_data['shipping_depth'],
        "shipping_height": form.cleaned_data['shipping_height'],
        "shipping_price": form.cleaned_data['shipping_price'],
        "shipping_width": form.cleaned_data['shipping_width'],
        "shipping": form.cleaned_data['shipping'],
        "sku_simple": form.cleaned_data['sku_simple'],
        "weight": form.cleaned_data['weight'],
        "weight_unit": form.cleaned_data['weight_unit'],
        "category_pk": form.cleaned_data['category_pk']
    }
    if images_urls:
        data['images'] = images_urls
    return json.dumps(data)


def get_data_product_variations(form):
    images_urls = []
    if form.cleaned_data['image01'] != '':
        images_urls.append({'url': form.cleaned_data['image01']})
    try:
        if form.cleaned_data['image02'] != '':
            images_urls.append({'url': form.cleaned_data['image02']})
    except Exception:
        pass

    variation01 = {
        'price': form.cleaned_data['var01_price'],
        'sku': form.cleaned_data['var01_sku'],
        'stock': form.cleaned_data['var01_stock'],
        'part_number': form.cleaned_data['var01_part__number'],
        'images': {
            'url': form.cleaned_data['var01_image01']
        }
    }
    variation02 = {
        'price': form.cleaned_data['var02_price'],
        'sku': form.cleaned_data['var02_sku'],
        'stock': form.cleaned_data['var02_stock'],
        'part_number': form.cleaned_data['var02_part_number'],
        'images': {
            'url': form.cleaned_data['var02_image01']
        }
    }

    data = {
        "price": form.cleaned_data['price'],
        "sku": form.cleaned_data['sku'],
        "stock": form.cleaned_data['stock'],
        "name": form.cleaned_data['name'],
        "brand": form.cleaned_data['brand'],
        "description": form.cleaned_data['description'],
        "dimensions_unit": form.cleaned_data['dimensions_unit'],
        "shipping_depth": form.cleaned_data['shipping_depth'],
        "shipping_height": form.cleaned_data['shipping_height'],
        "shipping_price": form.cleaned_data['shipping_price'],
        "shipping_width": form.cleaned_data['shipping_width'],
        "shipping": form.cleaned_data['shipping'],
        "sku_simple": form.cleaned_data['sku_simple'],
        "weight": form.cleaned_data['weight'],
        "weight_unit": form.cleaned_data['weight_unit'],
        "category_pk": form.cleaned_data['category_pk'],
        "variations": [variation01, variation02]
    }
    if images_urls:
        data['images'] = images_urls
    return json.dumps(data)
