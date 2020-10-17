from flask import Flask,request,abort,jsonify
import simplejson as json

from validator import RequestInputSchema as req_val
from payment_gateway_factory import PaymentGatewayFactory

app= Flask(__name__)

@app.route("/payment/process",methods=['POST'])
def ProcessPayment():
    req= request.json
    errors = req_val().validate(req)
    print(req)
    print(errors)
    if errors:
        abort(400)
    
    gateway_factory = PaymentGatewayFactory()
    res= gateway_factory.process_payment(req['amt'])
    return res

if __name__ == "__main__":
    app.run()