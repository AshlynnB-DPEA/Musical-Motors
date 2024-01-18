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

    def stopMotor(self):
        print("b")
        #dpiStepper.setSpeedInRevolutionsPerSecond(0, 0)
        dpiStepper.decelerateToAStop(0)


    def c3(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .082)
        dpiStepper.moveToRelativePositionInRevolutions(0, 10000, False)

    def cshp3(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .087)
        dpiStepper.moveToRelativePositionInRevolutions(0, 10000, False)

    def d3(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .0923)
        dpiStepper.moveToRelativePositionInRevolutions(0, 10000, False)

    def dshp3(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .097)
        dpiStepper.moveToRelativePositionInRevolutions(0, 10000, False)

    def e3(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .1036)
        dpiStepper.moveToRelativePositionInRevolutions(0, 10000, False)

    def f3(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .109)
        dpiStepper.moveToRelativePositionInRevolutions(0, 10000, False)

    def fshp3(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .1151)
        dpiStepper.moveToRelativePositionInRevolutions(0, 10000, False)

    def g3(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0,.1225)
        dpiStepper.moveToRelativePositionInRevolutions(0, 10000, False)

    def gshp3(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .13)
        dpiStepper.moveToRelativePositionInRevolutions(0, 10000, False)

    def a3(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .1375)
        dpiStepper.moveToRelativePositionInRevolutions(0, 10000, False)

    def ashp3(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .1463)
        dpiStepper.moveToRelativePositionInRevolutions(0, 10000, False)

    def b3(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .1545)
        dpiStepper.moveToRelativePositionInRevolutions(0, 10000, False)

    def c4(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .1644)
        dpiStepper.moveToRelativePositionInRevolutions(0, 10000, False)

    def cshp4(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .174)
        dpiStepper.moveToRelativePositionInRevolutions(0, 10000, False)

    def d4(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .185)
        dpiStepper.moveToRelativePositionInRevolutions(0, 10000, False)

    def dshp4(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .195)
        dpiStepper.moveToRelativePositionInRevolutions(0, 10000, False)

    def e4(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .2065)
        dpiStepper.moveToRelativePositionInRevolutions(0, 10000, False)

    def f4(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .21935)
        dpiStepper.moveToRelativePositionInRevolutions(0, 10000, False)

    def fshp4(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .232)
        dpiStepper.moveToRelativePositionInRevolutions(0, 10000, False)

    def g4(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .245)
        dpiStepper.moveToRelativePositionInRevolutions(0, 10000, False)

    def gshp4(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .261)
        dpiStepper.moveToRelativePositionInRevolutions(0, 10000, False)

    def a4(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .27515)
        dpiStepper.moveToRelativePositionInRevolutions(0, 10000, False)

    def ashp4(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .2913)
        dpiStepper.moveToRelativePositionInRevolutions(0, 10000, False)

    def b4(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .31)
        dpiStepper.moveToRelativePositionInRevolutions(0, 10000, False)

    def c5(self):
        dpiStepper.setSpeedInRevolutionsPerSecond(0, .327)
        dpiStepper.moveToRelativePositionInRevolutions(0, 10000, False)











if __name__ == "__main__":
    KeyboardApp().run()
