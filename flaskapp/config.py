  class Config(object):
    """
    Common configurations
    
    """

  class DevelopmentConfig(Config):
    """
    Development Configurations

    """

    DEBUG = True
    SQLALCHEMY_ECHO = True

  class ProductionConfig(Config):
    """
    Production configurations
    
    """
    DEBUG = False

  app_config = {
    'development': DevelopmentConfig,
    'production': PRoductionConfig
  }
