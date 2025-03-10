'''
Test for the health check api
'''

from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient


class HealthCheckApiTests(TestCase):
    '''Test the health check api'''

    def setUp(self):
        self.client = APIClient()

    def test_health_check_api(self):
        '''Test the health check api'''
        url = reverse('health-check')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'status': 'ok'})
