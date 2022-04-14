from django.urls import path

from orders import views

app_name = "orders"

urlpatterns = [
    # ORDER QUATOTION
    path(
        "list/quatotion/",
        views.list_order_quatotion,
        name="list_order_quatotion",
    ),
    path(
        "search/list/quatotion/",
        views.search_list_order_quatotion,
        name="search_list_order_quatotion",
    ),
    path(
        "create-quatotion/",
        views.create_order_quatotion,
        name="create_order_quatotion",
    ),
    path(
        "update-quatotion/<int:order_quatotion_pk>/",
        views.update_order_quatotion,
        name="update_order_quatotion",
    ),
    path(
        "delete-quatotion/<int:order_quatotion_pk>/",
        views.delete_order_quatotion,
        name="delete_order_quatotion",
    ),
    path(
        "orderitemquatotion_set/testlab/unit_quantity_price/",  # be carefull about the _ because of the http request htmx
        views.quatotion_testlab_unit_quantity_price,
        name="quatotion_testlab_unit_quantity_price",
    ),
    path(
        "pdf/quatotion/<int:order_quatotion_pk>/",
        views.pdf_quatotion_order,
        name="pdf_quatotion_order",
    ),
    path(
        "pdf/requirement/<int:order_quatotion_pk>/",
        views.pdf_requirement_order,
        name="pdf_requirement_order",
    ),
    path(
        "csv/quatotion/",
        views.csv_quatotion_order,
        name="csv_quatotion_order",
    ),
    # ORDER EXECUTION
    path(
        "edit-execution/<int:order_execution_pk>/",
        views.edit_order_execution,
        name="edit_order_execution",
    ),
    path(
        "orderitemexecution_set/testlab/unit_quantity_price/",  # be carefull about the _ because of the http request htmx
        views.execution_test_lab_unit_quantity_price,
        name="execution_test_lab_unit_quantity_price",
    ),
    path(
        "pdf/execution/<int:order_execution_pk>/",
        views.pdf_execution_order,
        name="pdf_execution_order",
    ),
    # ORDER LIQUIDATION
    path(
        "edit-liquidation/<int:order_liquidation_pk>/",
        views.edit_order_liquidation,
        name="edit_order_liquidation",
    ),
    path(
        "orderitemliquidation_set/testlab/unit_quantity_price/",  # be carefull about the _ because of the http request htmx
        views.liquidation_testlab_unit_quantity_price,
        name="liquidation_testlab_unit_quantity_price",
    ),
    path(
        "pdf/liquidation/<int:order_liquidation_pk>/",
        views.pdf_liquidation_order,
        name="pdf_liquidation_order",
    ),
    # ORDER INFO
    path(
        "edit-info/<int:order_quatotion_pk>",
        views.edit_order_quatotion_info,
        name="edit_order_quatotion_info",
    ),
]
