from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PostsConfig(AppConfig):
    name = 'monthtera.posts'
    verbose_name = _("Posts")

    def ready(self):
        try:
            import monthtera.posts.signals
        except ImportError:
            pass
