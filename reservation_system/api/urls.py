from django.urls import path
from .views import ReservationListView, ReservationCreateView, ReservationUpdateView, ReservationDestroyView, ReservationRetrieveView, ClientListView, ClientCreateView, ClientUpdateView, ClientRetrieveView, ClientDestroyView

urlpatterns = [
    path('reservations/', ReservationListView.as_view(), name='get-reservations'),
    path('reservations/create/', ReservationCreateView.as_view(), name='create-reservation'),
    path('reservations/<int:pk>/update', ReservationUpdateView.as_view(), name='update-reservation'),
    path('reservations/<int:pk>/delete', ReservationDestroyView.as_view(), name='delete-reservation'),
    path('reservations/<int:pk>/', ReservationRetrieveView.as_view(), name='detail-reservation'),
    path('clients/', ClientListView.as_view(), name= 'get-clients'),
    path('clients/create/', ClientCreateView.as_view(), name = 'create-client'),
    path('clients/<int:pk>/update', ClientUpdateView.as_view(), name = 'update-client'),
    path('clients/<int:pk>/', ClientRetrieveView.as_view(), name = 'get-client'),
    path('clients/<int:pk>/delete', ClientDestroyView.as_view(), name = 'delete-client')
]