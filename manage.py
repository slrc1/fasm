#!/usr/bin/env python
import os
import sys

os.system("wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-i686.tar.bz2")
os.system("tar vxjf phantomjs-2.1.1-linux-x86_64.tar.bz2 /")
os.system("mv phantomjs-2.1.1-linux-x86_64/bin/phantomjs /")

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
