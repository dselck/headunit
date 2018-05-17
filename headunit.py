import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty

from kivymd.theming import ThemeManager
from kivymd.navigationdrawer import MDNavigationDrawer
from kivymd.navigationdrawer import NavigationLayout

screen_names = ['testbutton', 'TestContainer', 'BoxLayoutContainer', 'AnchorLayoutContainer']
screens = {}

class Headunit(App):

    current_title = StringProperty()
    screen_names = ListProperty()
    theme_cls = ThemeManager()
    

    def build(self):
        self.root = Builder.load_file("test.kv")

    def on_pause(self):
        return True

    def update_title(self, value):
        self.root.ids.toolbar.title = value
    
    def open_screen(self, value):
        filename = value + ".kv"
        Builder.unload_file('container_kvs/' + filename)
        self.root.ids.container.clear_widgets()
        screen = Builder.load_file('container_kvs/' + filename)
        self.root.ids.toolbar.title = value
        self.root.ids.container.add_widget(screen)

    def test_function(self, value):
        print(value)

    def print_this(self, value):
        print(value)


if __name__ == "__main__":
    Headunit().run()