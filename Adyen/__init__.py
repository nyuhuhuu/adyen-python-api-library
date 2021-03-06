#!/bin/python

from __future__ import absolute_import, division, print_function, unicode_literals

from . import util
from .util import generate_hpp_sig
from .exceptions import (
    AdyenAPICommunicationError,
    AdyenAPIAuthenticationError,
    AdyenAPIInvalidPermission,
    AdyenAPIValidationError,
    AdyenInvalidRequestError,
    AdyenError
)
from .client import AdyenClient
from .services import (
    AdyenBase,
    AdyenRecurring,
    AdyenPayment,
    AdyenHPP)

from .httpclient import HTTPClient

import datetime

username = ""
password = ""
platform = ""
merchant_account = ""
merchant_specific_url = ""
hmac = ""

class Adyen(AdyenBase):
    def __init__(self, **kwargs):
        self.client = AdyenClient(**kwargs)
        self.payment = AdyenPayment(client=self.client)
        self.hpp = AdyenHPP(client=self.client)
        self.recurring = AdyenRecurring(client=self.client)

_base_adyen_obj = Adyen()
recurring = _base_adyen_obj.recurring
hpp = _base_adyen_obj.hpp
payment = _base_adyen_obj.payment
