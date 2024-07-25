from django.test import TestCase
from django.contrib.auth.models import User
from .models import Car
from django.utils.dateparse import parse_datetime

class CarModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')
        cls.car = Car.objects.create(
            model='Model S',
            brand='Tesla',
            price=79999.99,
            is_bought=True,
            buyer=cls.user,
            buy_time=parse_datetime('2024-01-01T00:00:00Z')
        )

    def test_car_creation(self):
        self.assertEqual(self.car.model, 'Model S')
        self.assertEqual(self.car.brand, 'Tesla')
        self.assertEqual(self.car.price, 79999.99)
        self.assertTrue(self.car.is_bought)
        self.assertEqual(self.car.buyer.username, 'testuser')
        
        # Parse datetime string to a datetime object for comparison
        expected_buy_time = parse_datetime('2024-01-01T00:00:00Z')
        self.assertEqual(self.car.buy_time, expected_buy_time)
