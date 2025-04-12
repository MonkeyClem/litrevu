from django.urls import path
from .views import create_review, edit_review, delete_review

urlpatterns = [
    path('create/<int:ticket_id>/', create_review, name='create_review'),
    path('<int:review_id>/edit/', edit_review, name="edit_review"),
    path('<int:review_id>/delete/', delete_review, name='delete_review')
]