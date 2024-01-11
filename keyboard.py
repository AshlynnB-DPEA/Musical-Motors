import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from dpeaDPi.DPiComputer import DPiComputer
from dpeaDPi.DPiStepper import *
from kivy.uix.label import Label
from kivy.uix.screenmanager import *
from kivy.clock import *

sm = ScreenManager()
dpiStepper = DPiStepper()
dpiStepper.setBoardNumber(0)
dpiStepper.enableMotors(True)

"""
speed_in_mm_per_sec = 70
accel_in_mm_per_sec_per_sec = 150
dpiStepper.setSpeedInMillimetersPerSecond(0, speed_in_mm_per_sec)
dpiStepper.setAccelerationInMillimetersPerSecondPerSecond(0, accel_in_mm_per_sec_per_sec)
wait_to_finish_moving_flg = False

"""
stepper_num = 0
gear_ratio = 1
motorStepPerRevolution = 1600 * gear_ratio
dpiStepper.setStepsPerRevolution(stepper_num, motorStepPerRevolution)

speed_in_revolutions_per_sec = 2.0
accel_in_revolutions_per_sec_per_sec = 2.0
dpiStepper.setSpeedInRevolutionsPerSecond(stepper_num, speed_in_revolutions_per_sec)
dpiStepper.setAccelerationInRevolutionsPerSecondPerSecond(stepper_num, accel_in_revolutions_per_sec_per_sec)



class KeyboardApp(App):
    def build(self):
        sm.add_widget(Keyboard())
        return sm


class Keyboard(Screen):

    def run_motor(self):
        dpiStepper.moveToRelativePositionInRevolutions(0, 0.1, False)

    Clock.schedule_interval(run_motor, 0.1)



    def stopMotor(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, 0)

    def c3(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .082)

    def cshp3(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .087)

    def d3(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .0923)

    def dshp3(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .097)

    def e3(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .1036)

    def f3(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .109)

    def fshp3(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .1151)

    def g3(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0,.1225)

    def gshp3(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .13)

    def a3(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .1375)

    def ashp3(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .1463)

    def b3(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .1545)

    def c4(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .1644)

    def cshp4(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .174)

    def d4(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .185)

    def dshp4(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .195)

    def e4(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .2065)

    def f4(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .21935)

    def fshp4(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .232)

    def g4(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .245)

    def gshp4(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .261)

    def a4(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .27515)

    def ashp4(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .2913)

    def b4(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .31)

    def c5(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .327)











if __name__ == "__main__":
    KeyboardApp().run()
