from django.conf import settings as django_settings

class AppSettings:

    _prefix = "EVENT_"

    defaults = {
        "DISPATCHER_CLASS": "django_events.dispatchers.AsyncIODispatcher",
        "STORAGE_CLASS": "django_events.storages.AsyncIOQueue",
        "STORAGE_OPTIONS": {},
    }

    def __init__(self, prefix=None, defaults={}):
        self._prefix = prefix or AppSettings._prefix

        defaults = dict(self.defaults, **defaults)
        for name, default in defaults.items():
            value = getattr(django_settings, self._prefix + name, default)
            setattr(self, name, value)
    
    def __getattr__(self, key):
        return self.key

settings = AppSettings()