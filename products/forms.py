from django import forms


class SimpleProductForm(forms.Form):
    sku = forms.CharField(label='SKU', max_length=40, initial='TESTL009K2HHM0')
    stock = forms.IntegerField(label='Stock', initial=1)
    price = forms.FloatField(label='Precio', initial=20)
    name = forms.CharField(label='Nombre Producto', max_length=255)
    brand = forms.CharField(label='Marca de Producto', max_length=255)
    description = forms.CharField(label='Descripción de Producto', max_length=255)
    image01 = forms.URLField(label='Url Imagen 1')
    dimensions_unit = forms.CharField(label='Descripción de Producto', max_length=2, initial='cm')
    shipping_depth = forms.FloatField(label='Shipping depth', initial=0)
    shipping_height = forms.FloatField(label='shipping_height', initial=0)
    shipping_price = forms.FloatField(label='shipping_price', initial=0)
    shipping_width = forms.FloatField(label='shipping_width', initial=0)
    shipping = forms.IntegerField(label='shipping', initial=0)
    sku_simple = forms.CharField(label='sku_simple', max_length=100, initial='TESTL009K2HHM0')
    weight = forms.FloatField(label='weight', initial=0)
    weight_unit = forms.CharField(label='weight_unit', initial='kg')
    category_pk = forms.IntegerField(label='Category pk', initial=520)


class OtherSimpleProductForm(SimpleProductForm):
    image02 = forms.URLField(label='Url Imagen 2')


class VariationProductForm(SimpleProductForm):
    image02 = forms.URLField(label='Url Imagen 2', required=False)

    var01_price= forms.FloatField(label='Variación 1 Precio', initial=20)
    var01_sku= forms.CharField(label='Variación 1 SKU', max_length=40, initial='TESTL009K2HHM0-00')
    var01_stock = forms.IntegerField(label='Variación 1 Stock', initial=1),
    part01_part_number = forms.CharField(label='Variación 1 Part Number', max_length=40, initial='TESTL009K2HHM0-00')
    var01_image01 = forms.URLField(label='Variación 1 Url Imagen 1', required=False)

    var02_price = forms.FloatField(label='Variación 2 Precio', initial=20)
    var02_sku = forms.CharField(label='Variación 2 SKU', max_length=40, initial='TESTL009K2HHM0-00')
    var02_stock = forms.IntegerField(label='Variación 2Stock', initial=1),
    part02_part_number = forms.CharField(label='Variación 2 Part Number', max_length=40, initial='TESTL009K2HHM0-00')
    var02_image01 = forms.URLField(label='Variación 2 Url Imagen 1', required=False)