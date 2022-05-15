class Config:
    '''
    General configuration parent class
    '''

    QUOTES_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    

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