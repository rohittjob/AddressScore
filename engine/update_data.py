from data_processor.generator import *
from pincode_util import *

FILE_PATH = join(ROOT, 'data_processor', 'data', 'latest_data.dat')
TRAINING_DATA_FILE = join(ROOT, 'data_processor', 'data', 'training_data.dat')

def update_data():
    print 'Updating Data... ',
    f = open(FILE_PATH, 'w')
    generate(f)
    update_information(FILE_PATH)
    print 'Finished'
    f = open(FILE_PATH, 'r')
    training_file = open(TRAINING_DATA_FILE,'a')
    training_file.write(f.read())
    training_file.close()
    f.close()
    os.remove(FILE_PATH)


if __name__ == '__main__':
    update_data()