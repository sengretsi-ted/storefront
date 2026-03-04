from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Customer, Product, Collection, Order, OrderItem

# using the render function to render a template
def say_hello(request):

    # keyword=value
    # queryset = Product.objects.filter(unit_price_gt=20)

    # all products that contain the word 'coffee' in their title
    # queryset = Product.objects.filter(title__icontains='coffee')

    # all products that were updated in 2021
    # queryset = Product.objects.filter(last_update__year=2021)

    # 1. customers with .com accounts
    # queryset = Customer.objects.filter(email__icontains='.com')

    # 2. collections that don't have a featured product
    # queryset = Collection.objects.filter(featured_product__isnull=True)

    # 3. Products with low inventory (less than 10)
    # queryset = Product.objects.filter(inventory__lt=10)

    # 4. Orders placed by customers with id = 1
    # queryset = Order.objects.filter(customer__id=1)

    # 5. Order items for products in colleciton 3
    # queryset = OrderItem.objects.filter(product__collection__id=3)

    # exists = Product.objects.filter(pk=0).exists()
    
    # query_set.filter().filter().order_by()

    # for product in query_set:
    #     print(product)

    # query_set[0:5] 

    return render(request, 'hello.html', {'name':'Ted', 'products': list(queryset)})


