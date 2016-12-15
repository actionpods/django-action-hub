=====
Action Hub
=====

Action Hub is a django app that creates and encourages new leaders in activism both to start their own movements and coordinate with others to make real change.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'action-hub',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^action-hub/', include('action-hub.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Visit http://127.0.0.1:8000/action-hub/
