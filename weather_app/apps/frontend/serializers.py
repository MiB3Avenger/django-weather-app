from rest_framework import serializers

from .models import CityData


class CityDataSerializer(serializers.ModelSerializer):
    # Custom field names for city data.
    coord = serializers.SerializerMethodField('coordinates')
    name = serializers.SerializerMethodField('nameCapitalize')
    country = serializers.SerializerMethodField('countryUpper')
    
    # Capitalize first letter of city name.
    def nameCapitalize(self, cityData):
        return cityData.name.capitalize()
    
    # All caps for country.
    def countryUpper(self, cityData):
        return cityData.country.upper()

    # Convert latitude and longitude into coordinate format.
    def coordinates(self, cityData):
        return {'lat': cityData.lat, 'lon': cityData.lon}
    
    class Meta:
        model = CityData
        fields = ['name', 'country', 'coord']