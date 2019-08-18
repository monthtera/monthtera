from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SubscriptionsConfig(AppConfig):
    name = 'monthtera.subscriptions'
    verbose_name = _("Subscriptions")

    def ready(self):
        try:
            import monthtera.subscriptions.signals
        except ImportError:
            pass
