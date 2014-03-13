#pylint: skip-file
import atexit
import os
import psutil
import subprocess
import threading
import time

COMMAND = 'python manage.py runserver 8111 --noreload'


def start():
    cmd = COMMAND
    verbose = os.environ.get('VERBOSE')
    if not verbose:
        cmd += ' > /dev/null 2>&1'
    os.system(cmd)


def kill_django():
    command = COMMAND.split()
    for p in psutil.process_iter():
        try:
            if p.cmdline() == command:
                p.terminate()
                print('Shut down test API...')
        except:
            pass
    remove_db()


def remove_db():
    try:
        os.remove(os.path.join('/dev', 'shm', 'db.sqlite3'))
    except OSError:
        pass


def run():
    atexit.register(kill_django)
    os.chdir(os.path.join('tests', 'testsite'))
    remove_db()
    subprocess.check_call('python manage.py syncdb --noinput'.split())
    subprocess.check_call('python manage.py createsuperuser --noinput --username=testuser --email=none@test.test'.split())
    t = threading.Thread(target=start)
    t.daemon = True
    t.start()
    subprocess.check_call('python manage.py user'.split())

run()
