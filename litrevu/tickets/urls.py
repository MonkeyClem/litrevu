from django.urls import path
from .views import  create_or_edit_ticket, create_ticket_and_rewiew
from .views import delete_ticket

urlpatterns = [
    path('create_ticket/', create_or_edit_ticket, name='create_ticket'),
    path('create_ticket_and_review/', create_ticket_and_rewiew, name = "create_ticket_and_rewiew"),
    path('<int:ticket_id>/edit/', create_or_edit_ticket, name="edit_ticket" ),
    path('<int:ticket_id>/delete/', delete_ticket, name="delete_ticket" ),
]

