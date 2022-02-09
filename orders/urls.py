from django.urls import path

from orders.views import list_order, create_order, update_order, delete_order, create_order_item_row, characteristic_test_lab, test_lab_price, delete_order_item_row, company_project_client

app_name = 'orders'

urlpatterns = [
    # order
    path('list/', list_order, name='list_order_hx'),
    path('create-order/', create_order, name='create_order'),
    path('update-order/<int:order_id>/', update_order, name='update_order'),
    path('delete-order/<int:order_id>/', delete_order, name='delete_order_hx'),
    # orderitems
    path('add-row/', create_order_item_row, name='create_order_item_row_hx'),
    path('delete-row/<int:order_item_id>/', delete_order_item_row,
         name='delete_order_item_row_hx'),
    # be carefull about the _ because of the http request
    path('characteristic/test_lab/', characteristic_test_lab,
         name='characteristic_test_lab_hx'),
    path('test_lab/price/', test_lab_price, name='test_lab_price_hx'),
    path('company/project/client/', company_project_client,
         name='company_project_client_hx')
]
