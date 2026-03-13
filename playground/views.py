from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, DecimalField # for complex queries using OR, AND, NOT
from django.db.models import Count, Min, Max, Avg, Sum # for aggregations
from django.db.models import Value, F, Func, ExpressionWrapper # for annotations
from django.db.models.functions import Concat # for concatenating fields in annotations
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
        # queryset = Product.objects.filter(
        #         id__in=OrderItem.objects.values('product_id').distinct()
        # ).order_by('title')
        

        """Deferring fields"""
        # Get all products don't defer the description and last_update fields
        # queryset = Product.objects.only('id', 'title')

        # Get all products but defer the description and last_update fields
        # queryset = Product.objects.defer('description', 'last_update')

        """Selecting related objects"""
        # Using select_related (1) to fetch the related collection for each product in a single query
        # queryset = Product.objects.select_related('collection').all()

        # Using prefetch_related (n) to fetch the related order items for each product in a single query
        # queryset = Product.objects.prefetch_related(
                # 'promotions').select_related('collection').all()

        # Get last 5 orders with customer and items (including product)
        # queryset = Order.objects.select_related(
                # 'customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

        """Aggregating Objects"""
        # result = Product.objects.aggregate(
        #         count = Count('id'), min_price = Min('unit_price'))

        # number of products in each collection
        # result = Product.objects.aggregate(count = Count('id'))

        # number of orders 
        # result = Order.objects.aggregate(orders = Count('id'))

        # number of units of product 1 sold
        # result = OrderItem.objects.filter(product_id=1).aggregate(units_sold = Sum('quantity'))

        # total orders placed by customer 1
        # result = Order.objects.filter(customer_id=1).aggregate(orders_placed = Count('id'))

        # result = Product.objects.filter(collection=3).aggregate(
        #         min_price = Min('unit_price'),
        #         max_price = Max('unit_price'),
        #         average_price = Avg('unit_price')
        # )


        """Annotating Objects"""
        # queryset = Customer.objects.annotate(is_new = Value(True))

        # queryset = Customer.objects.annotate(new_id=F('id') + 1)

        """Calling Database Functions"""
        # queryset = Customer.objects.annotate(
        #         # CONCAT
        #         full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')
        # )

        # queryset = Customer.objects.annotate(
        #         full_name = Concat('first_name', Value(' '), 'last_name')
        # )

        """Grouping Data"""
        # queryset = Customer.objects.annotate(
        #         orders_count=Count('order')
        # )

        """Working with Expression Wrappers"""
        # discounted_price = ExpressionWrapper(
        #         F('unit_price') * 0.8, output_field=DecimalField())
        # queryset = Product.objects.annotate(
        #         discounted_price=discounted_price
        # )

        # customers with their last order ID
        # queryset = Customer.objects.annotate(last_order_id=Max('order__id'))

        # Collections and count of their products
        # queryset = Collection.objects.annotate(products_count=Count('product'))
        
        # Customers with more than 5 orders
        # queryset = Customer.objects.annotate(
        #         orders_count=Count('order')).filter(orders_count__gt=5)

        # Customers and the total amount they've spent
        # queryset = Customer.objects.annotate(
        #     total_spent=Sum(F('order__orderitem__quantity') * F('order__orderitem__unit_price'))
        # )

        # Top 5 products by total sales
        # queryset = Product.objects.annotate(
        #         total_sales=Sum(F('orderitem__quantity')*F('orderitem__unit_price'))
        # ).order_by('-total_sales')[:5]




        return render(request, 'hello.html', {'name':'Ted', 'result': list(queryset)})



