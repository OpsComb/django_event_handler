from asyncio.queues import Queue
import asyncio
from .base import BaseStorage

class AsyncQueue(BaseStorage):

    def __init__(self, storage_options, *args, **kwargs):
        self.storage = Queue()
    
    async def queue_task(self, task, **kwargs):
        if kwargs.pop('async', True):
            return await self.storage.put(task)
        else:
            return self.storage.put_nowait(task)
    
    async def get_task(self, **kwargs):
        if kwargs.pop('async', True):
            return await self.storage.get()
        else:
            self.storage.get_nowait()
    
    def check_empty(self, **kwargs):
        return self.storage.qsize() == 0