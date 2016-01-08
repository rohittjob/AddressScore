from data_processor.generator import *
from data_processor.cruncher import *
from utilities.config import DEBUG
from sklearn.naive_bayes import GaussianNB
import os


ROOT = dirname(get_dir(__file__))
FILE_PATH = join(ROOT, 'data_processor', 'data', 'training_data.dat')

keys = ['User_Rating', 'Timeliness', 'Product_Quality', 'Ease_of_Delivery', 'Quality_of_Delivery', 'Logistics_Cost']
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

    print 'Calculating Weights... ',
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


if __name__ == '__main__':
    print get_weights()






