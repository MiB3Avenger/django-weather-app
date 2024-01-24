from rest_framework import serializers

from .models import CityData


class CityDataSerializer(serializers.ModelSerializer):
    # Custom field names for city data.
    coord = serializers.SerializerMethodField('coordinates')
    country = serializers.SerializerMethodField('countryUpper')
    
    # All caps for country.
    def countryUpper(self, cityData):
        return cityData.country.upper()

    # Convert latitude and longitude into coordinate format.
    def coordinates(self, cityData):
        return {'lat': cityData.lat, 'lon': cityData.lon}
    
    class Meta:
        model = CityData
        fields = ['name', 'country', 'coord']