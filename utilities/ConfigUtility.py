import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                         "../config/config.ini"))


class ConfigReader:

    @staticmethod
    def getDesiredCapabilities():
        desired_caps = {}
        desired_caps['platformName'] = config.get('Capabilities', 'platformName')
        desired_caps['platformVersion'] = config.get('Capabilities', 'platformVersion')
        desired_caps['deviceName'] = config.get('Capabilities', 'deviceName')
        desired_caps['app'] = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../app/" + config.get('Capabilities', 'appName')))

        return desired_caps
