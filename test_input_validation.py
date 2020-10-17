import unittest
import simplejson as json
from datetime import datetime
import requests

from payment_gateway_api import app

class TestRequestInput(unittest.TestCase):

    @staticmethod
    def datetime_serial(dt):
        if isinstance(dt,datetime):
            return dt.__str__()
    
    def test_invalid_date(self):
        payload = json.dumps({
            "credit_card_num": "2356897845125689",
            "card_holder": "Amit Randive",

            "exp_date": datetime(2020, 5, 17),

            "security_code": "235",

            "amt": 125.0
        },default=TestRequestInput.datetime_serial)
        
        response = requests.post('http://127.0.0.1:5000/payment/process', data=payload,headers={'Content-type':'application/json'})
        self.assertEqual(400, response.status_code)
    
    def test_invalid_credit_card_no(self):
        payload = json.dumps({
            "credit_card_num": "235689784512",
            "card_holder": "Amit Randive",

            "exp_date": datetime(2020, 12, 17),

            "security_code": "235",

            "amt": 125.0
        },default=TestRequestInput.datetime_serial)
        
        response = requests.post('http://127.0.0.1:5000/payment/process', data=payload, headers={'Content-type':'application/json'})
        self.assertEqual(400, response.status_code)

    def test_invalid_security_code(self):
        payload = json.dumps({
            "credit_card_num": "2356897845125689",
            "card_holder": "Amit Randive",

            "exp_date": datetime(2020, 12, 17),

            "security_code": "23556",

            "amt": 125.0
        },default=TestRequestInput.datetime_serial)
        
        response = requests.post('http://127.0.0.1:5000/payment/process', data=payload, headers={'Content-type':'application/json'})
        self.assertEqual(400, response.status_code)

   # def test_invalid_amount(self):
   #     payload = json.dumps({
   #         "credit_card_num": "2356897845125689",
   #         "card_holder": "Amit Randive",
   #         "exp_date": datetime(2020, 12, 17),
   #        "security_code": "234",
   #        "amt":125
   #     },default=TestRequestInput.datetime_serial)
        
   #     response = requests.post('http://127.0.0.1:5000/payment/process', data=payload, headers={'Content-type':'application/json'})
   #     self.assertEqual(400, response.status_code)

    def test_invalid_amount(self):
        payload = json.dumps({
            "credit_card_num": "2356897845125689",
            "card_holder": "Amit Randive",
            "exp_date": datetime(2020, 12, 17),
            "security_code": "234",
            "amt":-125.0
        },default=TestRequestInput.datetime_serial)
        
        response = requests.post('http://127.0.0.1:5000/payment/process', data=payload, headers={'Content-type':'application/json'})
        self.assertEqual(400, response.status_code)