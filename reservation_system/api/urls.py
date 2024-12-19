from django.urls import path
from .views import ReservationListView, ReservationCreateView, ClientListView, ClientCreateView, ClientUpdateView, ClientRetrieveView, ClientDestroyView

urlpatterns = [
    path('reservations/', ReservationListView.as_view(), name='get_reservations'),
    path('reservations/create/', ReservationCreateView.as_view(), name='create_reservation'),
    path('clients/', ClientListView.as_view(), name= 'get_clients'),
    path('clients/create/', ClientCreateView.as_view(), name = 'create_client'),
    path('clients/<int:pk>/update', ClientUpdateView.as_view(), name = 'update_client'),
    path('clients/<int:pk>/', ClientRetrieveView.as_view(), name = 'get_client'),
    path('clients/<int:pk>/delete', ClientDestroyView.as_view(), name = 'delete_client')
]