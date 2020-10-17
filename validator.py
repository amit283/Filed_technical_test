from marshmallow import Schema, fields,ValidationError
from marshmallow.validate import Length

import decimal
from datetime import datetime


def validate_amount(val):
    print(isinstance(val,decimal.Decimal))
    if val > 0 and isinstance(val,decimal.Decimal):
        return True
    else:
        raise ValidationError("Amount must be positive decimal number")

class RequestInputSchema(Schema):
    """
    Validation Parameters:
    - CreditCardNumber (mandatory, string, it should be a valid credit card number)
    - CardHolder: (mandatory, string)
    - ExpirationDate (mandatory, DateTime, it cannot be in the past)
    - SecurityCode (optional, string, 3 digits)
    - Amount (mandatoy decimal, positive amount)
    """
    credit_card_num = fields.Str(required=True,validate=Length(min=16,max=16))
    card_holder = fields.Str(required=True)
    exp_date = fields.DateTime(required=True,validate=lambda d: d > datetime.now())
    security_code = fields.Str(validate=Length(min=3,max=3))
    amt = fields.Decimal(required=True,validate=validate_amount)

