from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework import status
from .models import Client, Reservation
from .serializer import ClientSerializer, ReservationSerializer

# Reservation Endpoints
class ReservationListView(ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationCreateView(CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationDestroyView(DestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationRetrieveView(RetrieveAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationUpdateView(UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    

# Client Endpoints
class ClientCreateView(CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientListView(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDestroyView(DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientUpdateView(UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientRetrieveView(RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer