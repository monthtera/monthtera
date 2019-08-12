from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BrandsConfig(AppConfig):
    name = "monthtera.brands"
    verbose_name = _("Brands")

    def ready(self):
        try:
            import monthtera.brands.signals  # noqa F401
        except ImportError:
            pass
