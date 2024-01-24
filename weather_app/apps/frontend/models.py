from django.db import models

# Model for City data.
"""
This model will store geodata along with it's name, state and country.
With this, when making searches, we can use pivot or foreign keys to fetch on the detail page.
More ease of access would be to eliminate Open Weather API fetch data which is already in the model.
But it is beyond scope for now.
"""
class CityData(models.Model):
    # Even though city with longer names are not widely used, but we'll prepare for them anyway.
    name = models.CharField(max_length=170)
    slug = models.CharField(max_length=170)
    lat = models.FloatField()
    lon = models.FloatField()
    country = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Model for City Details
"""
This model will store forecast data for the next 4 days.
Fetch new data if 1 hour has been passed since the last `updated_at` attribute.
"""
class CityDetail(models.Model):
    city = models.ForeignKey(CityData, on_delete=models.CASCADE)
    detail = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)