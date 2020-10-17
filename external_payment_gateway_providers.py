from abc import ABCMeta , abstractmethod

class IExternalPaymentGatewayProviders(metaclass=ABCMeta):
    @abstractmethod
    def is_service_available(self):
        pass

    @abstractmethod
    def call_service(self):
        pass

    @abstractmethod
    def retry_available(self):
        pass

    @abstractmethod
    def change_service_availibility(self,availability):
        pass