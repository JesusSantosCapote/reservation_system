from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Client, Reservation
from .serializer import ClientSerializer, ReservationSerializer

class ReservationViewsTests(APITestCase):
    def setUp(self):
        self.client_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
        }
        self.client_obj = Client.objects.create(**self.client_data)
        
        self.reservation_data = {
            'client': self.client_obj,
            'reservation_date': '2024-12-19',
            'status': 'PENDING'
        }
        self.reservation = Reservation.objects.create(**self.reservation_data)

    def test_reservation_list(self):
        url = reverse('get-reservations')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_reservation_create(self):
        url = reverse('create-reservation')
        new_reservation = {
            'client': self.client_obj.id,
            'reservation_date': '2024-12-20',
            'status': 'PENDING'
        }
        response = self.client.post(url, new_reservation, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reservation.objects.count(), 2)

    def test_reservation_retrieve(self):
        url = reverse('detail-reservation', args=[self.reservation.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['client'], self.client_obj.id)

    def test_reservation_update(self):
        url = reverse('update-reservation', args=[self.reservation.id])
        updated_data = {
            'client': self.client_obj.id,
            'reservation_date': '2024-12-20',
            'status': 'CANCELED'
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'CANCELED')

    def test_reservation_delete(self):
        url = reverse('delete-reservation', args=[self.reservation.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Reservation.objects.count(), 0)