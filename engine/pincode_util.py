from engine.scorer import *
from data_processor.cruncher import *
from utilities.config import PINCODE_INDEX, DEBUG
import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = "portal.settings"
django.setup()

from location.models import *


ROOT = dirname(get_dir(__file__))
FILE_PATH = join(ROOT, 'data_processor', 'data', 'training_data.dat')


def update_pincode_score(new_scores, pincode):
    pin_obj = Pincode.objects.get_or_create(pincode=pincode)[0]
    new_encountered_entries = pin_obj.encountered_entries + new_scores[1]
    pin_obj.score = (pin_obj.score*pin_obj.encountered_entries + new_scores[0])/new_encountered_entries
    pin_obj.encountered_entries = new_encountered_entries
    pin_obj.save()


def update_information(file_path):
    f = open(file_path, 'r')
    feedback_set = pickle.load(f)

    print 'Normalizing feedback... ',
    for i in range(len(feedback_set)):
        feedback_set[i] = normalize(feedback_set[i])

    pin_to_scores = {}
    for feedback in feedback_set:
        score = get_score(feedback)
        pincode = feedback[PINCODE_INDEX]
        if not pin_to_scores.has_key(pincode):
            pin_to_scores[pincode] = [0.0,0]
        pin_to_scores[pincode][0] += score
        pin_to_scores[pincode][1] += 1

    if not DEBUG:
        print 'Updating pincode scores... ',
        for pincode in pin_to_scores.keys():
            update_pincode_score(pin_to_scores[pincode], pincode)


if __name__ == '__main__':
    update_information(FILE_PATH)