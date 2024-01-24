import json
from typing import Tuple
from django.conf import settings

from datetime import datetime, timedelta

from pyowm.owm import OWM
from pyowm.geocodingapi10.geocoding_manager import GeocodingManager
from pyowm.weatherapi25.weather_manager import WeatherManager
from pyowm.weatherapi25.forecaster import Forecaster

from .forms import CityDataForm, CityDetailForm
from .models import CityData, CityDetail
from .exceptions import OWMInitError

class FrontendService:
    owm: OWM
    
    def __init__(self) -> None:
        """
        When class is initialized, create OWM SDK using API Key.

        Raises:
            OWMInitError
        """
        # Create OWM handler.
        try:
            self.owm = OWM(settings.OWM_API_KEY)
        except:
            raise OWMInitError("Cannot initialize OWM")
    
    def geocodeManager(self) -> GeocodingManager:
        """
        Create a geocoding manager and raise exception if OWM SDK is not initialized.

        Raises:
            OWMInitError

        Returns:
            GeocodingManager: Geocoding Manager to be used for searching cities.
        """
        # Create geocoding manager or throw error if OWM is not initialized.
        if self.owm:
            return self.owm.geocoding_manager()
        else:
            raise OWMInitError("OWM is not initialized for geocoding manager.")
    
    def getCityByName(self, name: str) -> list|dict:
        """
        Fetch city based on name from geocode manager.

        Args:
            name (str): Name of the city.

        Returns:
            list|dict: List of cities or errorful dictionary.
        """
        # Create geocoding manager.
        try:
            geocodingManager = self.geocodeManager()
        except OWMInitError as e:
            return {'success': False, 'message': 'Cannot create open weather maps sdk.', 'error': e.message}
        
        # Search for location.
        try:
            return geocodingManager.geocode(name, limit=5)
        except:
            return {'success': False, 'message': 'Cannot search for cities right now.'}
    
    def weatherManager(self) -> WeatherManager:
        """
        Create a weather manager and raise exception if OWM SDK is not initialized.

        Raises:
            OWMInitError

        Returns:
            WeatherManager: Weather Manager to be used for searching city forecasts.
        """
        # Create weather manager or throw error if OWM is not initialized.
        if self.owm:
            return self.owm.weather_manager()
        else:
            raise OWMInitError("OWM is not initialized for weather manager.")
        
    def getCityWeather(self, coord: dict) -> Forecaster|dict:
        """
        Get city weather for 5 days in 3 hour intervals.

        Args:
            coord (dict): Co-ordinates for location with {lat, lon} keys.

        Returns:
            Forecaster|dict: Get forecast or errorful dictionary.
        """
        # Create weather manager.
        try:
            weatherManager = self.weatherManager()
        except OWMInitError as e:
            return {'success': False, 'message': 'Cannot create open weather maps sdk.', 'error': e.message}
        
        # Search for location.
        try:
            return weatherManager.forecast_at_coords(lat=coord['lat'],lon=coord['lon'], interval='3h').forecast
        except:
            return {'success': False, 'message': 'Cannot search for cities right now.'}
    
    def cityDataFormValidate(self, body: list) -> Tuple[bool, str]:
        """
        Validates City Data from request body.

        Args:
            body (list): The request body

        Returns:
            Tuple[bool, str]: Returns true or false, along with error messages.
        """
        # Check if form submission is valid or send errorful string.
        cityDataForm = CityDataForm(body)
        
        if cityDataForm.is_valid():
            return True, ''
        else:
            return False, cityDataForm.errors.as_json()
    
    def cityDetailFormValidate(self, body: list) -> Tuple[bool, str]:
        """
        Validates City Detail from request body.

        Args:
            body (list): The request body

        Returns:
            Tuple[bool, str]: Returns true or false, along with error messages.
        """
        # Check if form submission is valid or send errorful string.
        cityDetailForm = CityDetailForm(body)
        
        if cityDetailForm.is_valid():
            return True, ''
        else:
            return False, cityDetailForm.errors.as_json()
    
    def fetchCityData(self, name: str = None, slug: str = None, country: str = None) -> CityData|None:
        """
        Fetch city data from our database.

        Args:
            name (str): Name of the city.
            slug (str): Slugified name of the city.
            country (str): Name of the country the city is in.

        Returns:
            CityData|None: Found city data or None to validate incoming data.
        """
        # Simple get CityData object.
        try:
            if slug and country:
                return CityData.objects.get(slug__exact=slug, country__exact=country)
            
            if name and slug and country:
                return CityData.objects.get(name__exact=name, slug__exact=slug, country__exact=country)
                
            if country:
                return CityData.objects.get(name__exact=name, country__exact=country)
            return CityData.objects.get(name__exact=name)
        except CityData.DoesNotExist:
            return None
        
    def storeCityData(self, data: list) -> CityData:
        """
        Store our city data and get it's object for further use.

        Args:
            data (list): Form data for city data.

        Returns:
            CityData: If data is valid, then stored data is returned in CityData instance object.
        """
        # Check validation, just in case.
        valid, error = self.cityDataFormValidate(data)
        if valid:
            cityDataForm = CityDataForm(data)
            
            cityDataForm.save()
            
            return self.fetchCityData(data['name'])
        else:
            raise Exception(error)
    
    def fetchCityDetails(self, cityData: CityData) -> CityDetail|None:
        """
        Fetch city details.

        Args:
            cityData (CityData): CityData object to fetch it's details

        Returns:
            CityDetail|None: Return either city details or None
        """
        # Simple get CityDetail object.
        try:
            return CityDetail.objects.get(city=cityData)
        except CityDetail.DoesNotExist:
            return None
        
    def storeCityDetails(self, cityData: CityData, data: list, cityDetail: CityDetail = None) -> CityDetail:
        form = {
            'city': cityData,
            'detail': data['weathers']
        }
        
        # Check for validation, just in case.
        valid, error = self.cityDetailFormValidate(form)
        if valid:
            # Get city detail, if it doesn't exists, then we'll create. If it does exist, we'll update.
            if not cityDetail:
                cityDetailForm = CityDetailForm(form)
                
                cityDetailForm.save()
            else:
                updateCityDetail = CityDetail(id=cityDetail.id, city=cityData, detail=data['weathers'], created_at=cityDetail.created_at)
                updateCityDetail.save()
            
            return self.fetchCityDetails(cityData)
        else:
            raise Exception(error)
    
    def check3hDifference(self, set_date: datetime) -> bool:
        """
        Check if there has been a change for 3 hours from the set_date and now.

        Args:
            set_date (datetime): Any datetime instance object

        Returns:
            (bool): Gives answer to 3 hour difference from the set_date and now.
        """
        now = datetime.now()
        set_date = set_date.replace(tzinfo=None)
        
        # Simple check for 3 hour past set_date.
        return ((now - set_date) / 60 * 60) > timedelta(hours=3)