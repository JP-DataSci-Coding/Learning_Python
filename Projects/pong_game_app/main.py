from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector

# A widget is an element of a graphical user interface (GUI) that displays information or provides a specific way
# for a user to interact with the operating system or an application

# The Widget class is the base class required for creating Widgets, think of it as the main UI canvas


class PongGame(Widget):
    pass

# The App class is the base for creating Kivy applications. Think of it as your main entry point into the Kivy
# run loop. In most cases, you subclass this class and make your own app. You create an instance of your specific app
# class and then, when you are ready to start the application’s life cycle, you call your instance’s App.run() method.


class PongBall(Widget):
    # Velocity of the ball on the x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # ReferenceListProperty so we can use ball.velocity as a shorthand, just like e.g. w.pos for w.x and w.y
    velocity = ReferenceListProperty(velocity_x, velocity_y)


class PongApp(App):
    def build(self):
        # Creates an instance of our PongGame Widget class and returns it as the root element for the applications UI,
        # which you should imagine at this point as a hierarchical tree of Widgets.
        return PongGame()


# Used to execute some code only if the file was run directly, and not imported.
if __name__ == '__main__':
    PongApp().run()
