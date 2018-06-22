import visa

visa.log_to_screen()
rm = visa.ResourceManager()
print(rm.list_resources())
my_instrument = rm.open_resource('GPIB0::10::INSTR')
print (my_instrument)
my_instrument.query('*IDN?')
