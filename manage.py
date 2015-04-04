#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "whats_fresh.settings")

    if "syncdb" in sys.argv:
        print("\033[91msyncdb has been deprecated\033[0m")
        exit(1)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
