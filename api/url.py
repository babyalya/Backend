from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from bags.views import api_view
from bags.views import*




urlpatterns = [
    
    path('user/', manage_user, name='get_users'),  
    path('user/<int:id>/', manage_user, name='get_users'),
    # path('update/<int:pk>/', update_student),

    path('payment/', manage_payment, name='get_payment'),  
    path('payment/<int:id>/', manage_payment, name='get_payment'), 

    # path('order_item/', manage_order_item, name='get_order_item'),
    # path('order_item/<int:id>/', manage_order_item, name='get_order_item'),

    path('product/', manage_product, name='get_product'),
    path('product/<int:id>/', manage_product, name='get_product'),

    path('categories/', manage_categories, name='get_categories'),
    path('categories/<int:id>/', manage_categories, name='get_categories'),

    path('customer/', manage_customer, name='get_customer'),
    path('customer/<int:id>/', manage_customer, name='get_customer'),

    path('order/', manage_order, name='get_order'),
    path('order/<int:id>/', manage_order, name='get_order'),

    path('supplier/', manage_suppliers, name='get_supplier'),
    path('supplier/<int:id>/', manage_suppliers, name='get_supplier'),
      
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
