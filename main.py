import visa
rm = visa.ResourceManager()
inst = rm.open_resource('GPIB0::10::INSTR')
print(inst.query('*IDN?\n'))
print(inst.query('SPEC?0\n'))
