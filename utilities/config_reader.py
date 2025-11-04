import configparser
import os

config = configparser.RawConfigParser()
config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'config.ini')
config.read(config_path)

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        return config.get('common info', 'baseURL')

    @staticmethod
    def getEmail():
        return config.get('common info', 'email')

    @staticmethod
    def getPassword():
        return config.get('common info', 'password')

    @staticmethod
    def isHeadless():
        return config.getboolean('common info', 'headless', fallback=True)
