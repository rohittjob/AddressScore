from engine.scorer import *
from engine.pincode_util import *


pin = input('Enter a pincode: ')
feed = [1,1,1,1,1,1,SUCCESS]
score = get_score(feed)
update_pincode_score([score,1], pin)


if pin < 100000 or pin > 999999:
    print 'Enter valid pincode'
