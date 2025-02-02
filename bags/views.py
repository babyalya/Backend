from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import*
from .serializers import*
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views import View
from rest_framework import viewsets
import json

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UsersSerializers


class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset=Categories.objects.all()
    serializer_class=CategoriesSerializers

class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomersSerializers

class OrderViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializers

class SuppliersViewSet(viewsets.ModelViewSet):
    queryset=Suppliers.objects.all()
    serializer_class=SuppliersSerializers  

class PaymentViewSet(viewsets.ModelViewSet):
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializers      


@permission_classes([IsAuthenticated])
def generic_api(model_class, serializer_class):
    @api_view(['GET', 'POST', 'PUT','DELETE'])
    def api(request, id=None):
        #for GET
        if request.method == 'GET':
            if id:
                try:
                    instance=model_class.objects.get(id=id)
                    serializer= serializer_class(instance)
                    return Response(serializer.data)
                except model_class.DoesNotExist:
                    return Response({'message': 'object not found'},status=404)
            else:
                instances=model_class.objects.all()
                serializer=serializer_class(instances, many=True)
                return Response(serializer.data)
         #for Insert   
        elif request.method == 'POST':
            serializer=serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        #for Update
        elif request.method == 'PUT':
            if id:
                try:
                    instance=model_class.objects.get(id=id)
                    serializer=serializer_class(instance, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                    return Response(serializer.errors, status=400)
                except model_class.DoesNotExist:
                    return JsonResponse({'message': 'object not found'},status=404)
            return Response({'message': 'id is required for update'}, status=400)
        # for Delete
        elif request.method == 'DELETE':
            if id:
                try:
                    instance = model_class.objects.get(id=id)
                    instance.delete()
                    return Response({'message': 'Deleted successfully'}, status=204)
                except model_class.DoesNotExist:
                    return JsonResponse({'message': 'Object not found'}, status=404)
            return Response({'message': 'ID is required for deletion'}, status=400)

        return JsonResponse({'message': 'Invalid method'}, status=405)

    return api


# API views for SYSTEM order
manage_user = generic_api(User, UsersSerializers)
manage_payment = generic_api(Payment, PaymentSerializers)
# manage_order_item = generic_api(Order_item, Order_itemSerializers)    
manage_product = generic_api(Product, ProductSerializers)    
manage_categories = generic_api(Categories, CategoriesSerializers)    
manage_customer = generic_api(Customer, CustomersSerializers)   
manage_order = generic_api(Order, OrderSerializers)   
manage_suppliers = generic_api(Suppliers, SuppliersSerializers)   


#update_student=generic_api(Student, StudentSerializer)


