""" TODO: Add docstring
"""

import logging
import json

from pywebio import output

# SETTINGS_FILE_NAME = "/root/.plebtools/settings.json"
SETTINGS_FILE_NAME = "./data/settings.json"

class AppSettings:
    """ TODO: Add docstring
    """
    def __init__(self) -> None:
        try:
            with open(SETTINGS_FILE_NAME, 'r', encoding="utf-8") as settings_file:
                self._settings_json = json.load( settings_file )
                logging.debug("Settings loaded: %s", self._settings_json)

        except FileNotFoundError:
            logging.warning("No settings file found, creating a new blank one")
            self._settings_json = {
                # bitcoin core RPC authentication
                'RPC_USER': '',
                'RPC_PASS': '',
                'RPC_HOST': '127.0.0.1',
                'RPC_PORT': '8332',

                # Braiins Pool API
                'BRAIINS_TOKEN': '',

                # Adafruit IO
                'ADAFRUIT_USERNAME': '',
                'ADAFRUIT_APITOKEN': '',

                # Twilio
                'TWILIO_SID': '',
                'TWILIO_TOKEN' : '',
                'TWILIO_PHONE_NUMBER': '',
                # E164 format: [+] [country code] [subscriber number including area code]
                'NOTIFY_PHONE_NUMBER': '',
            }
            self.save_settings()

    def save_settings(self):
        """Save settings to file"""

        if self._settings_json is None:
            logging.error("Settings not loaded, not saving")
            output.toast("Settings not loaded, not saving", duration=5, color='error')
            return

        with open(SETTINGS_FILE_NAME, 'w', encoding="utf-8") as settings_file:
            json.dump(self._settings_json, settings_file, indent=4)

        output.toast("Settings saved")

    def __getitem__(self, key):
        return self._settings_json[key]

    def __setitem__(self, key, value):
        self._settings_json[key] = value
