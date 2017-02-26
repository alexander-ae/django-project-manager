#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    from django.conf import settings

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise

    if 'test' in sys.argv:
        import logging

        # logging.disable(logging.CRITICAL)
        # settings.DEBUG = False
        # settings.TEMPLATE_DEBUG = False
        settings.PASSWORD_HASHERS = [
            'django.contrib.auth.hashers.MD5PasswordHasher',
        ]
        #settings.DATABASES = {
        #    'default': {
        #        'ENGINE': 'django.db.backends.sqlite3',
        #        'NAME': 'test',
        #    }
        #}
        settings.MIDDLEWARE_CLASSES = [
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
        ]

    if 'test' in sys.argv and '--time' in sys.argv:
        sys.argv.remove('--time')
        from django import test
        import time


        def setUp(self):
            self.startTime = time.time()


        def tearDown(self):
            total = time.time() - self.startTime
            if total > 0.5:
                print("\n\t\033[91m%.3fs\t%s\033[0m" % (total, self._testMethodName))

                test.TestCase.setUp = setUp
                test.TestCase.tearDown = tearDown

    execute_from_command_line(sys.argv)
