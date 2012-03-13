# encoding: utf-8
from django.db import models
from customers.widgets import AddressFormField

class Address(object):
    def __init__(self, street, number, postcode, town, province, region):
        self.street = street
        self.number = number
        self.postcode = postcode
        self.town = town
        self.province = province
        self.region = region

    def __unicode__(self):
        return "%s, N %s, %s, %s, %s, %s" % (self.street,
                                           self.number,
                                           self.postcode,
                                           self.town,
                                           self.province,
                                           self.region)

class AddressField(models.Field):
    description = " An address for an office or settlement "
    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        super(AddressField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if isinstance(value, Address):
            return value

        value = str(value)
        args = value.split(',')[:6]
        if len(args)<6:
            n = 6 - len(args)
            args.extend([None for i in xrange(n)])
        return Address(*args)

    def get_prep_value(self, value):
        return ','.join([value.street,
                         value.number,
                         value.postcode,
                         value.town,
                         value.province,
                         value.region])

    def formfield(self, **kwargs):
        defaults = {'form_class': AddressFormField}
        defaults.update(kwargs)
        print defaults
        return super(AddressField, self).formfield(**defaults)
