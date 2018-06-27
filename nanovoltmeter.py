import visa

rm = visa.ResourceManager()
inst = rm.open_resource('GPIB::7::INSTR')
#print(inst.query("*IDN?"))

def m_voltage():
    inst.write("*RST")
    inst.write(":INITiate:CONTinuous OFF;:ABORt")
    inst.write(":SENSe:FUNCtion 'VOLTage:DC'")
    inst.write(":SENSe:VOLTage:DC:RANGe 1E-3")
    inst.write(":SENSe:VOLTage:DC:RANGe:AUTO ON")
    print("Voltage measured by nanovoltmeter is:\n")
    print(inst.query(":SENSe:DATA:LATest?"))
