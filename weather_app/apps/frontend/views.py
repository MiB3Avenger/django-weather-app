import json

from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .service import FrontendService
from .serializers import CityDataSerializer

from drf_yasg.utils import swagger_auto_schema

# Create your views here.
@swagger_auto_schema(
        method="GET",
        operation_id="v1/frontend/",
        operation_description="A default path for allowing django to serve API's V1 url to frontend.",
    )
@api_view(["GET"])
def frontend(request):
    return Response({'success': True}, status=status.HTTP_200_OK)


@swagger_auto_schema(
        method="GET",
        operation_id="v1/frontend/search/city/{name}",
        operation_description="Search for city endpoint",
    )
@api_view(["GET"])
def searchCity(request, name: str):
    """
    Search a city using OpenWeatherMaps SDK. Requires city name to get result.

    Args:
        name (str): URL part to search for a city using name.

    Returns:
        Response
    """
    # Create frontend service
    frontendService = FrontendService()
    
    # Get geocode by name
    geocode = frontendService.getCityByName(name=name)
    
    if type(geocode) == 'dict':
        return Response(geocode, status=status.HTTP_400_BAD_REQUEST)
    
    if len(geocode) == 0:
        # Early exit if we don't get any data.
        return Response({'success': True, 'locations': []}, status=status.HTTP_200_OK)
    
    # Convert Location to dict with the range of cities returned.
    locationsMap = map(lambda x: geocode[x].to_dict(), range(len(geocode)))
    locationsDict = dict(zip(range(len(geocode)), locationsMap))
    
    # Create an empty response list.
    locations = []
    
    # Remove duplicate values.
    for item in range(len(geocode)):
        # Search for name and if not exists in list, then append to the list.
        if locationsDict[item]['name'] not in [locations[i]['name'] for i, x in enumerate(locations)]:
            locations.append(locationsDict[item])
    
    # Return list of searches.
    return Response({'success': True, 'locations': locations}, status=status.HTTP_200_OK)


@swagger_auto_schema(
        method="POST",
        operation_id="v1/frontend/store/city",
        operation_description="Store city endpoint using forms",
    )
@api_view(["POST"])
def storeCity(request):
    """
    Store city information in database and fetch it's latest details.
    """
    # Create frontend service.
    frontendService = FrontendService()
    
    # store request data into a body.
    body = request.data
    
    # Validate form.
    valid, error = frontendService.cityDataFormValidate(body)
    
    # If form is not valid, then ask user to change information.
    if not valid:
        return Response({"success": False, "errors": json.loads(error)}, status=status.HTTP_400_BAD_REQUEST)
    
    # Fetch city, and if it's not stored, then create new row and get it's details.
    cityData = frontendService.fetchCityData(body['name'])
    
    if not cityData:
        data = body.copy()
        data['name'] = data['name'].lower()
        data['country'] = data['country'].upper()
        cityData = frontendService.storeCityData(data) # Returns city data.
    
    # Check if we have details, and hasn't been updated in last hour.
    cityDetails = frontendService.fetchCityDetails(cityData)
    
    # If city details is not present or 3 hours has been passed since last update, then we'll fetch new data.
    if not cityDetails or frontendService.check3hDifference(cityDetails.updated_at):
        # Get data in dictionary format.
        cityWeather = frontendService.getCityWeather(coord={'lat': cityData.lat, 'lon': cityData.lon}).to_dict()
        # Store city weather into database.
        cityDetails = frontendService.storeCityDetails(cityData=cityData, data=cityWeather)
    
    return Response({"success": True, "weather": cityDetails.detail}, status=status.HTTP_200_OK)


@swagger_auto_schema(
        method="GET",
        operation_id="v1/frontend/search/city-detail/{name}",
        operation_description="Search for city details endpoint",
    )
@api_view(["GET"])
def searchCityDetail(request, name: str, country: str):
    """
    _summary_

    Args:
        name (str): _description_
        country (str): _description_

    Returns:
        Response
    """
    # Create frontend service
    frontendService = FrontendService()
    
    # Get city data by name
    cityData = frontendService.fetchCityData(name=name,country=country)
    
    if not cityData:
        return Response({"success": False}, status=status.HTTP_404_NOT_FOUND)
    
    # Get city details.
    cityDetails = frontendService.fetchCityDetails(cityData=cityData)
    
    # If city details is not present or 3 hours has been passed since last update, then we'll fetch new data.
    if not cityDetails or frontendService.check3hDifference(cityDetails.updated_at):
        # Get data in dictionary format.
        cityWeather = frontendService.getCityWeather(coord={'lat': cityData.lat, 'lon': cityData.lon}).to_dict()
        # Store city weather into database.
        cityDetails = frontendService.storeCityDetails(cityData=cityData, data=cityWeather)
        
    return Response({"success": True, "city": CityDataSerializer(cityData).data, "weather": cityDetails.detail})