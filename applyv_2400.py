from time import sleep
from pymeasure.instruments.keithley import Keithley2400

keithley = Keithley2400("GPIB::24") 

def applyv(voltage,compliance_current):
    keithley.reset()
    keithley.use_front_terminals()
    keithley.apply_voltage()
    keithley.measure_current(auto_range=True)
    keithley.compliance_current = compliance_current
    keithley.enable_source()
    keithley.source_voltage = voltage
    current = keithley.current

def shutdown_v():
    keithley.shutdown()
