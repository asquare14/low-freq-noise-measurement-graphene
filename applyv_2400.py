from time import sleep
from pymeasure.instruments.keithley import Keithley2400
import injecti_2400

keithley = Keithley2400("GPIB::24") #change the address here

voltage = 0  #set the value of voltage you want to apply
compliance_current = 1E-4 #set compliance current


def applyv():
    keithley.reset()
    keithley.use_front_terminals()
    keithley.apply_voltage()
    keithley.measure_current(auto_range=True)
    keithley.compliance_current = compliance_current
    keithley.enable_source()
    keithley.source_voltage = voltage
    current = keithley.current
    injecti_2400.inject_i()
    
def shutdown_v():
    keithley.shutdown()
