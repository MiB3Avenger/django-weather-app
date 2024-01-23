from django.urls import path

from .views import (
    frontend,
    searchCity,
    storeCity,
    searchCityDetail,
)

app_name = 'frontend'
urlpatterns = [
    path('', frontend, name="default"),
    path('search/city/<str:name>', searchCity, name="searchCity"),
    path('store/city', storeCity, name="storeCity"),
    path('search/city-detail/<str:country>/<str:name>', searchCityDetail, name="searchCityDetail"),
]