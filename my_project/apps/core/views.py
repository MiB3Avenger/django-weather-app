from django.http import HttpResponse
from django.views.generic import TemplateView


def ping(request):
    """
    Health check url, it should return simplest and fastest response possible.

    It is used for checking availability
    """
    return HttpResponse("ok")


class Index(TemplateView):
    """
    Vite example app here
    """
    title = "Project Name"
    template_name = "core/index.html"

    @property
    def test_data(self) -> dict:
        """
        Add dummy data to the demplate
        """
        return {
            "yes": True,
            "no": False,
            "none": None,
            "text": "Lorem ipsum dolor sit amet",
            "list": [
                123,
                True,
                False,
                None,
                {"key": "value"},
            ],
            "dict": {
                "foo": "bar",
                "eggs": "spam",
            },
        }
