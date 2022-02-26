from django.urls import path

from orders import views

app_name = "orders"

urlpatterns = [
    # order
    path("list/", views.list_order, name="list_order_hx"),
    path("create-order/", views.create_order, name="create_order"),
    path("update-order/<int:order_id>/", views.update_order, name="update_order"),
    path("delete-order/<int:order_id>/", views.delete_order, name="delete_order_hx"),
    path(
        "pdf-cost-quatotion-order/<int:order_id>/",
        views.pdf_cost_quatotion_order,
        name="pdf_cost_quatotion_order",
    ),
    path(
        "pdf-cost-requirement-order/<int:order_id>/",
        views.pdf_requirement_order,
        name="pdf_requirement_order",
    ),
    path(
        "pdf-execution-order/<int:order_id>/",
        views.pdf_execution_order,
        name="pdf_execution_order",
    ),
    path(
        "pdf-liquidation-order/<int:order_id>/",
        views.pdf_liquidation_order,
        name="pdf_liquidation_order",
    ),
    # orderitems
    path("add-row/", views.create_order_item_row, name="create_order_item_row_hx"),
    path(
        "delete-row/<int:order_item_id>/",
        views.delete_order_item_row,
        name="delete_order_item_row_hx",
    ),
    # be carefull about the _ because of the http request
    path(
        "characteristic/test_lab/",
        views.characteristic_test_lab,
        name="characteristic_test_lab_hx",
    ),
    path("test_lab/price/", views.test_lab_price, name="test_lab_price_hx"),
    path(
        "company/project/client/",
        views.company_project_client,
        name="company_project_client_hx",
    ),
]
