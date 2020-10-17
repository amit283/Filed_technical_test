import unittest
from datetime import datetime
import requests
import simplejson as json

class TestPaymentProcess(unittest.TestCase):

    @staticmethod
    def datetime_serial(dt):
        if isinstance(dt,datetime):
            return dt.__str__()
    
    def test_expensive_gateway(self):
        payload = json.dumps({
            "credit_card_num": "2356897845125689",
            "card_holder": "Amit Randive",
            "exp_date": datetime(2020, 12, 17),
            "security_code": "235",
            "amt": 125.0
        },default=TestPaymentProcess.datetime_serial)
        
        response = requests.post('http://127.0.0.1:5000/payment/process', data=payload,headers={'Content-type':'application/json'})
        self.assertEqual(200, response.status_code)
    
    def test_cheap_gateway(self):
        payload = json.dumps({
            "credit_card_num": "2356897845125689",
            "card_holder": "Amit Randive",
            "exp_date": datetime(2020, 12, 17),
            "security_code": "235",
            "amt": 12.0
        },default=TestPaymentProcess.datetime_serial)
        
        response = requests.post('http://127.0.0.1:5000/payment/process', data=payload,headers={'Content-type':'application/json'})
        self.assertEqual(200, response.status_code)

    def test_premium_gateway(self):
        payload = json.dumps({
            "credit_card_num": "2356897845125689",
            "card_holder": "Amit Randive",
            "exp_date": datetime(2020, 12, 17),
            "security_code": "204",
            "amt": 1125.0
        },default=TestPaymentProcess.datetime_serial)
        
        response = requests.post('http://127.0.0.1:5000/payment/process', data=payload,headers={'Content-type':'application/json'})
        self.assertEqual(200, response.status_code)
    
if __name__ == "__main__":
    unittest.main()