"""
Class contains base storage class to be inherited by other storage classes
"""

class BaseStorage:
    def init_storage(self, storage_options={}, *args, **kwargs):
        # It has to be explicity called so that init can be lazy if required
        raise NotImplementedError("This storage does not implement init_storage operation")

    def queue_task(self, task, **kwargs):
        """
        Queue a task object in storage
        """
        raise NotImplementedError("This storage does not implement queue_task operation")

    def get_task(self, **kwargs):
        """
        Get a task from storage
        """
        raise NotImplementedError("This storage does not implement get_task operation")
    
    def check_empty(self, **kwargs):
        """
        Check if there are more tasks to perform
        """
        raise NotImplementedError("This storage does not implement check_empty operation")

