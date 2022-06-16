import pinject

import eventHandler.listener.MainViewListener
from appRuntime import AppRuntime
from eventHandler.EventHandler import EventHandler
# from view.MainView import MainView

if __name__ == '__main__':
    # uiThread = threading.Thread(target=MainView().open, args=[])
    # uiThread.start()

    listeners = []
    class SomeBindingSpec(pinject.BindingSpec):
        def configure(self, bind):
            bind('listeners', to_instance=listeners)
            # bind('view', to_class=MainView)

    obj_graph = pinject.new_object_graph(binding_specs=[SomeBindingSpec()])
    runtime = obj_graph.provide(AppRuntime)

    listeners.append(obj_graph.provide(eventHandler.listener.MainViewListener.MainViewListener))

    runtime.startMainView()
    # view = obj_graph.provide(MainView)
    # view.open()



