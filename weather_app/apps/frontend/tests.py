from django.test import TestCase
from frontend.models import CityData, CityDetail

# Create your tests here.
class CityDataTestCase(TestCase):
    def setup(self):
        CityData.objects.create(
            name="Nagpur",
            lat=21.1498134,
            lon=79.0820556,
            country="IN",
            state="Maharashtra"
        )