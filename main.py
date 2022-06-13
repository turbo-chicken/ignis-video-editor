import pinject

from appRuntime import AppRuntime
from view.MainView import MainView

if __name__ == '__main__':
    # uiThread = threading.Thread(target=MainView().open, args=[])
    # uiThread.start()


    #runtime = AppRuntime()
    obj_graph = pinject.new_object_graph()
    # obj_graph = pinject.new_object_graph(modules=None, classes=[AppRuntime])
    # obj_graph.provide(SomeClass)  # would raise a NothingInjectableForArgError
    # obj_graph = pinject.new_object_graph(modules=None, classes=[SomeClass, Foo])
    some_class = obj_graph.provide(AppRuntime)
    view = obj_graph.provide(MainView)
    view.open()



