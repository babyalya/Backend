from rest_framework import serializers
from.models import *


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model=Categories
        fields='__all__'        


class CustomersSerializers(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'

        


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'


class SuppliersSerializers(serializers.ModelSerializer):
    class Meta:
        model=Suppliers
        fields='__all__'

        


class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields='__all__'