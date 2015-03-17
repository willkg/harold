#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    # If no DJANGO_SETTINGS_MODULE is specified, pick an appropriate
    # one.
    if not os.environ.get('DJANGO_SETTINGS_MODULE'):
        if 'test' in sys.argv:
            settings_module = 'harold.settings.test'
        else:
            settings_module = 'harold.settings.base'
        os.environ['DJANGO_SETTINGS_MODULE'] = settings_module
        
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
