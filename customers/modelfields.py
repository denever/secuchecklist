# encoding: utf-8
from django.db import models
from customers.widgets import AddressFormField
from urllib import urlencode

class Address(object):
    def __init__(self, street, number, postcode, town, province):
        self.street = street
        self.number = number
        self.postcode = postcode
        self.town = town
        self.province = province

    def __unicode__(self):
        return "%s,%s,%s,%s,%s" % (self.street,
                                       self.number,
                                       self.postcode,
                                       self.town,
                                       self.province)

    def __repr__(self):
        return self.__unicode__()

    def __eq__(self, other):
        if (isinstance(other, Address)):
            eq = self.street == other.street
            eq = eq and self.number == other.number
            eq = eq and self.postcode == other.postcode
            eq = eq and self.town == other.town
            eq = eq and self.province == other.province
            return eq
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def decompress(self):
        return [self.street,
                self.number,
                self.postcode,
                self.town,
                self.province]

    def mapurl(self):
        return 'http://maps.google.it/maps?' + urlencode({'om': '1',
                                                          'iwloc': 'addr',
                                                          'f': 'q',
                                                          'q': self.__unicode__(),
                                                          'hl': 'it', 'z': '15', 'ie': 'UTF8'})

class AddressField(models.Field):
    description = " An address for an office or settlement "
    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        super(AddressField, self).__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'VARCHAR(255)'

    def to_python(self, value):
        if isinstance(value, Address):
            return value

        value = str(value)
        args = value.split(',')[:5]
        if len(args)<5:
            n = 5 - len(args)
            args.extend([None for i in xrange(n)])
        return Address(*args)

    def get_prep_value(self, value):
        return ','.join([value.street,
                         value.number,
                         value.postcode,
                         value.town,
                         value.province])

    def formfield(self, **kwargs):
        defaults = {'form_class': AddressFormField}
        defaults.update(kwargs)
        return super(AddressField, self).formfield(**defaults)
