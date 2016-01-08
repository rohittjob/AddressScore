import pickle
from utilities.os_util import *
from utilities.constants import SUCCESS, FAILURE
from utilities.config import FAILURE_WEIGHT, SUCCESS_WEIGHT

ROOT = get_dir(__file__)
PROJECT_ROOT = dirname(ROOT)

WEIGHTS_FILE_PATH = join(ROOT, 'data', 'attribute_weights.dat')


def scorer(feedback, weights):
    attr_size = len(weights)
    score = 0.0
    total_weight = 0.0
    for i in range(attr_size):
        score += feedback[i]*weights[i]
        total_weight += weights[i]

    score /= total_weight

    if feedback[attr_size] == FAILURE:
        score = (1 - score)*FAILURE_WEIGHT
    else:
        score *= SUCCESS_WEIGHT

    return score


def get_score(feedback):
    weights_file = open(WEIGHTS_FILE_PATH, 'r')
    attr_weights = pickle.load(weights_file)
    weights_file.close()
    return scorer(feedback, attr_weights)





