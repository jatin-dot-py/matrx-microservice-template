# core\socket\core\app_factory.py
from matrx_utils.socket.core.service_factory import ServiceFactory
from src.scraper_service import ScrapeService
from matrx_utils.socket.core.app_factory import configure_factory

class AppServiceFactory(ServiceFactory):
    def __init__(self):
        super().__init__()
        self.register_service("scraper_service_v2", ScrapeService)

        # Register YOUR app's services using the inherited methods
        # self.register_multi_instance_service...

configure_factory(AppServiceFactory)