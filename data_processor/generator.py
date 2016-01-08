import pickle
import random
from utilities.os_util import *
from utilities.constants import QUALITY_MEASURE, EASE_MEASURE, STATUS
from utilities.config import SAMPLE_SIZE

keys = ['User_Rating', 'Timeliness', 'Product_Quality', 'Ease_of_Delivery', 'Quality_of_Delivery', 'Logistics_Cost']

ROOT = get_dir(__file__)
FILE_DIR = join(ROOT, 'data')



ATTRIBUTE_SIZE = len(keys)


def generate_random_feedback():

    random.seed()  # default cur sys time
    user_rating = random.randint(1, 5)  # rating from 1 to 5
    timeliness = random.randint(-48, 48) + random.random()  # time in hours (float) where 0 is the estimated time of delivery, +ve is late, -ve is early

    random.shuffle(QUALITY_MEASURE)
    product_quality = QUALITY_MEASURE[0]  # QUALITY_MEASURE = ['Horrible', 'Extremely Poor', 'Poor', 'Average', 'Good', 'Very Good', 'Excellent']

    random.shuffle(EASE_MEASURE)
    ease_of_deliverability = EASE_MEASURE[0]  # EASE_MEASURE = ['Easy', 'Medium', 'Hard']

    random.shuffle(QUALITY_MEASURE)
    delivery_quality = QUALITY_MEASURE[0]

    logistics_cost = (random.randint(1,20) + random.random()) * 1000  # in rupees

    status = STATUS[int(round(random.random()))]  # STATUS = ['SUCCESS', 'FAILURE']

    pincode = random.randint(210010, 229413)  #  generating for allahabad

    feedback = [user_rating, timeliness, product_quality, ease_of_deliverability, delivery_quality, logistics_cost, status, pincode]

    return feedback


def generate(file_obj):

    print 'Generating Random Data Set... ',
    feedback_set = []
    for i in range(SAMPLE_SIZE):
        feedback = generate_random_feedback()
        feedback_set.append(feedback)
          # generating SUCCESS or FAILURE randomly


    pickle.dump(feedback_set, file_obj)
    file_obj.close()




if __name__ == '__main__':
    file_path = join(FILE_DIR, 'training_data.dat')
    f = open(file_path, 'w')
    generate(f)


