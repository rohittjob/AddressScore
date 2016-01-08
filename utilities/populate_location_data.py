import os
import django
from utilities.os_util import *
os.environ["DJANGO_SETTINGS_MODULE"] = "portal.settings"
django.setup()

from location.models import *


ROOT = get_dir(__file__)
PROJECT_ROOT = dirname(ROOT)

DATA_DIR = join(ROOT, 'data')


def populate_state(country):
    states_file = open(join(DATA_DIR, 'state_list.txt'), 'r')
    states = states_file.readlines()
    state_filenames = []
    state_objects = []
    for i in range(len(states)):
        states[i] = states[i].strip('\n')
        state_obj = State(state=states[i], country=country)
        state_obj.save()
        state_objects.append(state_obj)

        state_filenames.append(states[i].lower().replace(' ', '_') + '.txt')

    states_file.close()
    return (state_filenames, state_objects)


def populate_cities(state_filenames, state_objects):

    states_size = len(state_filenames)
    for i in range(states_size):
        state_file = open(join(DATA_DIR, state_filenames[i]), 'r')
        cities = state_file.readlines()
        for city_info in cities:
            city, zip_start, zip_end = city_info.split(',')
            City(city=city, zip_start=zip_start, zip_end=zip_end, state=state_objects[i]).save()
        state_file.close()



if __name__ == '__main__':
    country = Country(country='India')
    country.save()
    state_filenames, state_objects = populate_state(country)
    populate_cities(state_filenames, state_objects)

