from django.test import TestCase
from .models import Customer, Order
from rest_framework.test import APIClient

class CustomerOrderTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer = Customer.objects.create(name="Brain Opiyo", code="21872")
        self.order = Order.objects.create(customer=self.customer, item="Laptop", amount=1200)

    def test_create_customer(self):
        response = self.client.post('/api/customers/', {'name': 'Lilian Akinyi', 'code': '67890'})
        self.assertEqual(response.status_code, 201)

    def test_create_order(self):
        response = self.client.post('/api/orders/', {'customer': self.customer.id, 'item': 'Phone', 'amount': 500})
        self.assertEqual(response.status_code, 201)
