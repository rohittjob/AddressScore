from data_processor.generator import *
from data_processor.cruncher import *
from utilities.config import DEBUG, ATTRIBUTE_DELTA_THRESHOLD
from sklearn.naive_bayes import GaussianNB
import os


ROOT = dirname(get_dir(__file__))
FILE_PATH = join(ROOT, 'data_processor', 'data', 'training_data.dat')
WEIGHTS_FILE_PATH = join(ROOT,'engine', 'data', 'attribute_weights.dat')

keys = ['User_Rating', 'Timeliness', 'Product_Quality', 'Ease_of_Deliverability', 'Quality_of_Deliveribility', 'Logistics_Cost']
ATTRIBUTE_SIZE = len(keys)


def calc_weights(clf):
    attr_weights = []
    for i in range(ATTRIBUTE_SIZE):
        test_features = [0]*ATTRIBUTE_SIZE
        test_features[i] = 1
        weight = clf.predict_proba([test_features])
        attr_weights.append(weight[0][0])

    return attr_weights


def train_bayes(features, labels):
    clf = GaussianNB()
    clf.fit(features, labels)
    return clf


def process_feedback(feedback_set):
    features = []
    labels = []
    print 'Normalizing feedback... ',
    for feedback in feedback_set:
        feature, label = crunch(feedback)
        features.append(feature)
        labels.append(label)

    return (features, labels)


def get_weights():

    print 'Recalculating Weights... ',
    if not DEBUG:
        f = open(FILE_PATH, 'w')
        generate(f)
    f = open(FILE_PATH, 'r')
    feedback_set = pickle.load(f)
    features, labels = process_feedback(feedback_set)
    classifier = train_bayes(features, labels)
    weights = calc_weights(classifier)
    f.close()
    os.remove(FILE_PATH)
    print 'Finished'
    return weights


def recalculate():

    print 'Calculating new weights... ',
    new_weights = get_weights()

    try:
        weights_file = open(WEIGHTS_FILE_PATH, 'r')
    except:
        print 'Weights file does not exist. Please restart manager.'
        exit()
    attr_weights = pickle.load(weights_file)
    weights_file.close()

    attr_number = len(attr_weights)

    total_delta = 0.0
    for i in range(attr_number):
        delta = (abs(new_weights[i] - attr_weights[i]))
        total_delta += delta

    average_delta = total_delta/attr_number

    if average_delta <= ATTRIBUTE_DELTA_THRESHOLD:
        print 'Weights updated... ',
        os.remove(WEIGHTS_FILE_PATH)
        weights_file = open(WEIGHTS_FILE_PATH, 'w')
        pickle.dump(new_weights, weights_file)
        weights_file.close()
    else:
        print 'Weights not updated... ',
    print 'Finished'


if __name__ == '__main__':
    recalculate()






