from time import sleep
from pymeasure.instruments.keithley import Keithley2400

keithley = Keithley2400("GPIB::26")

def inject_i(current,compliance_voltage):
    keithley.reset()
    keithley.use_front_terminals()
    keithley.apply_current()
    keithley.measure_voltage(auto_range=True)
    keithley.compliance_voltage = compliance_voltage
    keithley.enable_source()
    keithley.source_current = current
    voltage = keithley.voltage

def shutdown_i():
    keithley.shutdown()
