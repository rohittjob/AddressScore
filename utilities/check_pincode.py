import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = "portal.settings"
django.setup()

from location.models import *


def get_pincode_score(pincode):
    if Pincode.objects.filter(pincode=pincode).exists():
        pin = Pincode.objects.get(pincode=pincode)
        return pin.score

    else:
        return 0.0


if __name__ == '__main__':
    while True:
        try:
            pin = input('Enter a pincode: ')
            if pin < 100000 or pin > 999999:
                print 'Enter valid pincode'
            else:
                print 'The score is: ' + str(get_pincode_score(pin))

        except:
            print 'Enter valid pincode'
