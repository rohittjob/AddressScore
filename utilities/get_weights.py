import pickle
from utilities.os_util import *
from utilities.constants import SUCCESS, FAILURE
from utilities.config import FAILURE_WEIGHT, SUCCESS_WEIGHT

ROOT = get_dir(__file__)
PROJECT_ROOT = dirname(ROOT)

WEIGHTS_FILE_PATH = join(PROJECT_ROOT,'engine', 'data', 'attribute_weights.dat')

weights_file = open(WEIGHTS_FILE_PATH, 'r')
attr_weights = pickle.load(weights_file)
weights_file.close()
print attr_weights