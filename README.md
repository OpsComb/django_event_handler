# django-event-handler [![PyPI version](https://badge.fury.io/py/django-event-handler.svg)](https://badge.fury.io/py/django-event-handler)

A utility to handle events in django asynchronously !!

## Description
django-event-handler provides dispatcher interface and event manager for handling django events. This application uses strings to track events and call custom handlers for performing operations.

### How is it different from Django Signals Framework?
Django's signal processing is synchronous i.e signals execute in the same process(or thread) processing the previous code. This made necessary to have an async executor (like celery) even for small actions like sending emails. This projects intends to removing that limitation and make use of asyncio to make signal processing asynchronous.

## Installation
django-event-system requires python3 and django 3+(since django 3 has async support). To install, just run `pip install django-event-handler`

## Getting started
To get started add `"django_events"` to your `INSTALLED_APPS` in `settings.py`.


