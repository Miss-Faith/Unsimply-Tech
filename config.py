import os
from dotenv import load_dotenv, find_dotenv
load_dotenv()

class Config:
    '''
    General configuration parent class
    '''

    

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

class TestConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass 


config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}