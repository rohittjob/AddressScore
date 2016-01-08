import subprocess
from multiprocessing import Process
from utilities.time_management import *

from attribute_weight_trainer import *
from update_data import *
from utilities.config import CRON_WAIT_TIME, WEIGHT_UPDATION_WAIT_TIME


ROOT = get_dir(__file__)
PROJECT_ROOT = dirname(ROOT)

WEIGHTS_FILE_PATH = join(ROOT, 'data', 'attribute_weights.dat')

PORTAL_PROCESS_SCRIPT_PATH = join(PROJECT_ROOT, "website", "manage.py")
WEIGHTS_UPDATION_SCRIPT_PATH = join(PROJECT_ROOT, "engine", "weight_updation.py")


def start_portal():
    print 'Starting Django Manager... ',
    django_manager = subprocess.Popen(['python', PORTAL_PROCESS_SCRIPT_PATH, "runserver"], creationflags=subprocess.CREATE_NEW_CONSOLE)
    print 'Started with PID ' + str(django_manager.pid)
    return django_manager


def weight_updation():

    next_stop = get_now()
    while True:
        next_stop = next_stop + timedelta(minutes=WEIGHT_UPDATION_WAIT_TIME)
        print 'Weights Updater started sleeping at ' + get_time()
        alarm('Weights Updater', next_stop)
        print 'Weights Updater  Woke Up!!!'
        print 'Starting Weights Updater ... ',
        updater = subprocess.Popen(['python', WEIGHTS_UPDATION_SCRIPT_PATH])
        print 'Started with PID ' + str(updater.pid)
        updater.wait()


if __name__ == '__main__':
    weights = get_weights()
    weights_file = open(WEIGHTS_FILE_PATH, 'w')
    pickle.dump(weights, weights_file)
    weights_file.close()
    portal_process = start_portal()
    weights_updater = Process(target=weight_updation)

    weights_updater.start()


    while True:
        update_data()
        now = get_now()
        alarm_time = now + timedelta(minutes=CRON_WAIT_TIME)
        alarm('Updater', alarm_time)

    portal_process.terminate()


