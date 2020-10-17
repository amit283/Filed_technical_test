from expensive_payment_gateway import ExpensivePaymentGateway
from premium_payment_gateway import PremiumPaymentGateway
from cheap_payment_gateway import CheapPaymentGateway

class PaymentGatewayFactoryMeta(type):
    _instance=None
    def __call__(cls,*args,**kwargs):
        if not cls._instance:
            instance= super().__call__(*args,**kwargs)
            cls._instance=instance
        return cls._instance

class PaymentGatewayFactory(metaclass=PaymentGatewayFactoryMeta):
    def __init__(self):
        self.__gateway = None

    def choose_gateway(self, amt):
        if amt<=20:
            self.__gateway = CheapPaymentGateway()
        elif amt >20 and amt <=500:
            self.__gateway = ExpensivePaymentGateway()
        elif amt > 500:
            self.__gateway = PremiumPaymentGateway()

        return self.__gateway
    
    def process_payment(self,amount):
        self.choose_gateway(amount)
        if self.__gateway.is_service_available():
            return self.__gateway.call_service()
        else:
            retry_count = self.__gateway.retry_available()

            if isinstance(self.__gateway,ExpensivePaymentGateway):
                self.__gateway = CheapPaymentGateway()

            for r in range(retry_count):
                if self.__gateway.is_service_available():
                    return self.__gateway.call_service()

        return "500"