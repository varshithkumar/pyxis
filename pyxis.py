

import kivy
from kivy.uix.image import Image
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.slider import Slider
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from random import randint


# type of star
# distance from the star (display habitable zone)
# Gravity (g)
# Mass of the planet
# Composition : (common elements or compounds: H2O, Nitrogen, Carbon)
# Temperature
# Air pressure/ Air density
# Rotation period
# Revolution period across the orbit around the star


# Tardigrades
# Brine shrimp
# roundworm
# insect larvae
# mushrooms (fungi)
# algal lifeforms
# salamander
# chimp

root = FloatLayout()
b1 = Button(pos_hint={'x': 0, 'center_y': .5})
b2 = Button(pos_hint={'right': 1, 'center_y': .5})
root.add_widget(b1)
root.add_widget(b2)


class OrganismImageContainer(GridLayout):

    def __init__(self, **kwargs) -> None:
        super(OrganismImageContainer, self).__init__(**kwargs)

        self.cols = 2

        tardigradeImage = Image(source="data/tardigrade.png", keep_ratio=False)
        brineshrimpImage = Image(source="data/brineshrimp.png", keep_ratio=False)
        nematodeImage = Image(source="data/nematodes.png", keep_ratio=False)
        rotiferImage = Image(source="data/rotifers.png", keep_ratio=False)
        larvaeImage = Image(source="data/insectlarvae.png", keep_ratio=False)

        images = [tardigradeImage, brineshrimpImage, nematodeImage, rotiferImage, larvaeImage]

        for image in images:
            self.add_widget(image)







class PlanetCustomizerContainer(GridLayout):
 
    def __init__(self, **kwargs):
         
        # super function can be used to gain access
        # to inherited methods from a parent or sibling
        # class that has been overwritten in a class object.
        super(PlanetCustomizerContainer, self).__init__(**kwargs)
 
        # 4 columns in grid layout
        self.cols = 4
         
        # declaring the slider and adding some effects to it
        self.gravityControl = Slider(min = 0, max = 100)
        self.distanceFromStar = Slider(min = 50, max = 10000)
        self.planetaryMassControl = Slider(min = 0.01, max = 10000)
        self.temperatureControl = Slider(min = -273.15, max = 1000)
        self.airPressureControl = Slider(min = 1, max = 1000)
        self.rotationPeriodControl = Slider(min = 0.05, max = 1000)
        self.revolutionPeriodControl = Slider(min = 0.001, max = 1000)
          
 
        # 1st row - one label, one slider   
        self.add_widget(Label(text ='g (acceleration due to \n gravity)'))
        self.add_widget(self.gravityControl)
 
        # 2nd row - one label for caption,
        # one label for slider value
        self.add_widget(Label(text ='value of g in m/(s^2)'))
        self.gravityValue = Label(text ='0')
        self.add_widget(self.gravityValue)


        self.add_widget(Label(text ='distance from star'))
        self.add_widget(self.distanceFromStar)
 
        # 2nd row - one label for caption,
        # one label for slider value
        self.add_widget(Label(text ='distance in million km'))
        self.distanceFromStarValue = Label(text ='50')
        self.add_widget(self.distanceFromStarValue)





        self.add_widget(Label(text ='mass of the planet'))
        self.add_widget(self.planetaryMassControl)
 
        # 2nd row - one label for caption,
        # one label for slider value
        self.add_widget(Label(text ='mass in earth mass M⊕'))
        self.planetaryMassValue = Label(text ='0.01')
        self.add_widget(self.planetaryMassValue)



        self.add_widget(Label(text='temperature of the planet'))
        self.add_widget(self.temperatureControl)
        self.add_widget(Label(text ='temperature in degree \n celsius'))
        self.tempValue = Label(text="-273.15")
        self.add_widget(self.tempValue)


        
        self.add_widget(Label(text='atmospheric pressure'))
        self.add_widget(self.airPressureControl)
        self.add_widget(Label(text ='pressure in atm'))
        self.atmValue = Label(text="1")
        self.add_widget(self.atmValue)


        
        self.add_widget(Label(text='period of rotation'))
        self.add_widget(self.rotationPeriodControl)
        self.add_widget(Label(text ='period in earth days'))
        self.rotPeriodValue = Label(text="0.05")
        self.add_widget(self.rotPeriodValue)


        
        self.add_widget(Label(text='period of revolution'))
        self.add_widget(self.revolutionPeriodControl)
        self.add_widget(Label(text ='period in earth years'))
        self.revPeriodValue = Label(text="0.001")
        self.add_widget(self.revPeriodValue)



 
 
        # On the slider object Attach a callback
        # for the attribute named value
        self.gravityControl.bind(value = self.on_value_gravity)
        self.distanceFromStar.bind(value = self.on_value_distance_from_star)
        self.planetaryMassControl.bind(value = self.on_value_planetary_mass)
        self.temperatureControl.bind(value = self.on_value_temperature)
        self.airPressureControl.bind(value = self.on_value_atm)
        self.rotationPeriodControl.bind(value = self.on_value_rotation_period)
        self.revolutionPeriodControl.bind(value = self.on_value_revolution_period)
        
    # Adding functionality behind the slider
    # i.e when pressed increase the value
    def on_value_gravity(self, instance, gravity):
        self.gravityValue.text = "% d"% gravity

    def on_value_distance_from_star(self, instance, distance):
        self.distanceFromStarValue.text = "% d"% distance

    def on_value_planetary_mass(self, instance, mass):
        self.planetaryMassValue.text = "% 3f"% mass

    def on_value_temperature(self, instance, temperature):
        self.tempValue.text = "% 3f"% temperature

    def on_value_atm(self, instance, atm):
        self.airPressureControl = "% 3f"% atm

    def on_value_rotation_period(self, instance, rot_period):
        self.rotPeriodValue = "% 3f"% rot_period

    def on_value_revolution_period(self, instance, rev_period):
        self.revPeriodValue = "% 3f"% rev_period

class PyxisContainer(GridLayout):

    def __init__(self, **kwargs) -> None:
        super(PyxisContainer, self).__init__(**kwargs)

        self.cols = 3

        earthImage = Image(source="data/earth.png", keep_ratio=False)

        self.add_widget(OrganismImageContainer())
        self.add_widget(PlanetCustomizerContainer())
        self.add_widget(earthImage)


class PyxisApp(App):

    def build(self):
        pyxisContainer = PyxisContainer()
        return pyxisContainer 


if __name__ == '__main__':
    PyxisApp().run()
