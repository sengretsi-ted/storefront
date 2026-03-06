from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F # for complex queries using OR, AND, NOT
from store.models import Customer, Product, Collection, Order, OrderItem

# # using the render function to render a template
# def say_hello(request):

#     # keyword=value
#     # queryset = Product.objects.filter(unit_price_gt=20)

#     # all products that contain the word 'coffee' in their title
#     # queryset = Product.objects.filter(title__icontains='coffee')

#     # all products that were updated in 2021
#     # queryset = Product.objects.filter(last_update__year=2021)

#     # 1. customers with .com accounts
#     # queryset = Customer.objects.filter(email__icontains='.com')

#     # 2. collections that don't have a featured product
#     queryset = Collection.objects.filter(featured_product__isnull=True)

#     # 3. Products with low inventory (less than 10)
#     # queryset = Product.objects.filter(inventory__lt=10)

#     # 4. Orders placed by customers with id = 1
#     # queryset = Order.objects.filter(customer__id=1)

#     # 5. Order items for products in colleciton 3
#     # queryset = OrderItem.objects.filter(product__collection__id=3)

#     # exists = Product.objects.filter(pk=0).exists()
    
#     # query_set.filter().filter().order_by()

#     # for product in query_set:
#     #     print(product)

#     # query_set[0:5] 

#     return render(request, 'hello.html', {'name':'Ted', 'products': list(queryset)})


def say_hello(request):
        # Product: Inventory < 10 AND price < 20
        # queryset = Product.objects.filter(inventory__lt=10, unit_price__lt=20)

        # Product: Inventory < 10 OR price < 20 using 2 filter() methods
        # queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)

        # Product: Inventory < 10 OR price < 20 using Q objects
        # queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))

        # Product: Inventory < 10 AND price >= 20 using Q objects
        # queryset = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20)).filter(title__icontains='coffee')

        # Referencing Fields using F Objects
        # Product: Inventory = price using F objects
        # queryset = Product.objects.filter(inventory=F('unit_price'))

        # Product: Inventory = price using F objects
        # queryset = Product.objects.filter(inventory=F('unit_price'))

        # Product: Inventory = collection id using F objects
        # queryset = Product.objects.filter(inventory=F('collection__id'))

        # Sorting
        # product = Product.objects.order_by('unit_price')[0] 
        # or
        # product = Product.objects.order_by('unit_price').first()
        # or
        # product = Product.objects.order_by.latest('unit_price')

        # Limiting Results
        # Show the first 5 products
        # queryset = Product.objects.all()[5:10]

        # Selecting Fields to Query
        # Reading the ids and titles of all products
        # queryset = Product.objects.values('id', 'title')

        # Reading the ids, titles and collection titles of all products
        # queryset = Product.objects.values_list('id', 'title', 'collection__title')

        # Reading the collection titles of all products
        # queryset = OrderItem.objects.values('product_id').distinct() 

        # Select products that have been ordered and sort by title
        queryset = Product.objects.filter(
                id__in=OrderItem.objects.values('product_id').distinct()
        ).order_by('title')
        

        return render(request, 'hello.html', {'name':'Ted', 'products': list(queryset)})
