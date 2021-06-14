from django_events.conf import settings as app_settings
import importlib

class BaseDispatcher:
    
    def get_storage_class(self):
        storage_class = app_settings.get('STORAGE_CLASS')
        storage_options = app_settings.get('STORAGE_OPTIONS')
        StorageClass = importlib(storage_class)
        return StorageClass(storage_options)
