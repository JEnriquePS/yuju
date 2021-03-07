"""yuju URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from products.views import (HomeTemplateView, SimpleProductFormView,
                            OtherSimpleProductFormView,
                            VariationProductFormView,
                            SuccessTemplateView)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',
         HomeTemplateView.as_view(),
         name='home_product'),
    path('producto/simple/',
         SimpleProductFormView.as_view(),
         name='simple_product'),
    path('producto/other/simple/',
         OtherSimpleProductFormView.as_view(),
         name='other_simple_product'),
    path('producto/variation/',
         VariationProductFormView.as_view(),
         name='variation_product'),
    path('producto/simple/success/',
         SuccessTemplateView.as_view(),
         name='success_product'),
]
