import re
from django.forms import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.forms.fields import Field, RegexField, Select

phone_digits_re = re.compile(r'^((\+|00)39\s)?[0-9]{2,4}\s[0-9]{5,8}$')

class ITPhoneNumberField(Field):
    """
    A form field that validates Italian Phone numbers (fixed and mobile)
    The correct format is XX(XX) XXXXX(XXX). Italian prefixes are between 2
    and 4 digits long for fixed line and 3 digits for all mobile operators.
    Over all the number is between 10 and 11 digits long.
    '0039 XX(XX) XXXXX(XXX)' and '+39 XX(XX) XXXXX(XXX)' validate too, but the
    international prefix is stripped from the number.
    Spaces between prefixes and number are mandatory.
    """
    default_error_messages = {
        'invalid':_(u'Enter a valid phone number'),
    }

    def clean(self, value):
        value = super(ITPhoneNumberField, self).clean(value)
        if value == u'':
            return value

        n = phone_digits_re.search(value)

        if not n:
            raise ValidationError(self.error_messages['invalid'])

        # Import a list of valid prefixes
        from it_phones import PHONE_CHOICES, MOBILE_CHOICES

        # Split the number and, if present, strip the international prefix from the number
        m = value.split(" ")

        if (m[0] == '+39') or (m[0] == '0039'):
            del m[0]

        # Check if the number is no longer than 11 digits
        if (len(m[0]) + len(m[1])) > 11:
            raise ValidationError(self.error_messages['invalid'])

        # Check the prefix against a list of valid fixed and mobile prefixes
        if m[0] in PHONE_CHOICES or m[0] in MOBILE_CHOICES:
            return u'%s %s' % (m[0], m[1])

        raise ValidationError(self.error_messages['invalid'])
