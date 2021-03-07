import json

from django.conf import settings
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
import requests
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import SimpleProductForm, OtherSimpleProductForm, VariationProductForm
from .utils import get_data_product_simple, get_headers, \
    get_data_product_variations

PRODUCT_URL = 'https://api.software.madkting.com/shops/{shop_pk}/products/'


class HomeTemplateView(TemplateView):
    template_name = 'home.html'


class SimpleProductFormView(FormView):
    form_class = SimpleProductForm
    template_name = 'product01.html'

    def form_valid(self, form):
        url = PRODUCT_URL.format(shop_pk=settings.SHOP_PK)
        response = requests.post(url,
                                 headers=get_headers(),
                                 data=get_data_product_simple(form))
        if response.ok:
            return HttpResponseRedirect(self.get_success_url())
        else:
            self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('success_product')


class OtherSimpleProductFormView(FormView):
    form_class = OtherSimpleProductForm
    template_name = 'product02.html'

    def form_valid(self, form):
        url = PRODUCT_URL.format(shop_pk=settings.SHOP_PK)
        response = requests.post(url,
                                 headers=get_headers(),
                                 data=get_data_product_simple(form))
        if response.ok:
            return HttpResponseRedirect(self.get_success_url())
        else:
            self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('success_product')


class VariationProductFormView(FormView):
    form_class = VariationProductForm
    template_name = 'product02.html'

    def form_valid(self, form):
        url = PRODUCT_URL.format(shop_pk=settings.SHOP_PK)
        response = requests.post(url,
                                 headers=get_headers(),
                                 data=get_data_product_variations(form))
        if response.ok:
            return HttpResponseRedirect(self.get_success_url())
        else:
            self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('success_product')


class SuccessTemplateView(TemplateView):
    template_name = 'success.html'
