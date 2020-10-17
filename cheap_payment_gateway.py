from external_payment_gateway_providers import IExternalPaymentGatewayProviders

class CheapPaymentGateway(IExternalPaymentGatewayProviders):
    def __init__(self):
        self.__is_available = True
    
    def is_service_available(self):
        return self.__is_available

    def change_service_availibility(self,availability):
        self.__is_available = availability
        
    def call_service(self):
        self.__is_available = False
        print("Payment is being processed by CheapPaymentGateway service...")
        self.__is_available = True
        return "Payment is processed: 200 OK"

    def retry_available(self):
        return 0
