#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    # Set settings module to base if we didn't specify it
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "harold.settings.base")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
