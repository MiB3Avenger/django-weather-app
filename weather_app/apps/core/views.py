from django.views.generic import TemplateView


class Ping(TemplateView):
    """
    Health check url, it should return simplest and fastest response possible.

    It is used for checking availability
    """
    title = "Weather App - Ping"
    template_name = "core/ping.html"

class Index(TemplateView):
    """
    Vite example app here
    """
    title = "Weather App"
    template_name = "core/index.html"
