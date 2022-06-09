import threading

from appRuntime import AppRuntime
from view.MainView import MainView

if __name__ == '__main__':
    # uiThread = threading.Thread(target=MainView().open, args=[])
    # uiThread.start()


    runtime = AppRuntime()

    MainView().open()

