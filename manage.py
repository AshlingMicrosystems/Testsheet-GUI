#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import webbrowser
chrome_path = 'C:/Program Files/Google/Chrome/Application %s'
webbrowser.get(chrome_path).open('chrome://settings/clearBrowserData')
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#driver = webdriver.Chrome()
#river.get('chrome://settings/clearBrowserData')
#driver.find_element_by_xpath('//settings-ui').send_keys(Keys.ENTER)


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'staticimage.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
