import unittest

from payment_gateway_factory import PaymentGatewayFactory
from expensive_payment_gateway import ExpensivePaymentGateway
from premium_payment_gateway import PremiumPaymentGateway
from cheap_payment_gateway import CheapPaymentGateway


class TestPaymentGatewaySelection(unittest.TestCase):
    def test_cheap_gateway_selection(self):
        amount = 19.0
        factory= PaymentGatewayFactory()
        gateway = factory.choose_gateway(amount)
        self.assertTrue(isinstance(gateway,CheapPaymentGateway))
    
    def test_expensive_gateway_selection(self):
        amount = 230.0
        factory= PaymentGatewayFactory()
        gateway = factory.choose_gateway(amount)
        self.assertTrue(isinstance(gateway,ExpensivePaymentGateway))

    def test_premium_gateway_selection(self):
        amount = 560.0
        factory= PaymentGatewayFactory()
        gateway = factory.choose_gateway(amount)
        self.assertTrue(isinstance(gateway,PremiumPaymentGateway))