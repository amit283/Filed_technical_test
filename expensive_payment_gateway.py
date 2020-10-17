from external_payment_gateway_providers import IExternalPaymentGatewayProviders

class ExpensivePaymentGateway(IExternalPaymentGatewayProviders):
    def __init__(self):
        self.__is_available = True
        self.__retry_count = 1
    
    def is_service_available(self):
        return self.__is_available

    def change_service_availibility(self,availability):
        self.__is_available = availability
        
    def call_service(self):
        self.__is_available = False
        self.__retry_count -=1
        print("Payment is being processed by ExpensivePaymentGateway service...")
        self.__is_available = True
        return "200"

    def retry_available(self):
        return self.__retry_count