import visa
rm = visa.ResourceManager()
inst = rm.open_resource('GPIB0::10::INSTR')
print(inst.query('*IDN?\n'))

f = open("yaxis.txt","w+")
f.write(inst.query('SPEC?0\n'))
f.close()

f = open('yaxis.txt', 'r+')
n = f.read().replace(',','\n')
f.truncate(0)
f.close()

f = open('yaxis.txt','w+')
f.write(n)
f.close()

#print(inst.query('BVAL?0,0\n'))
#print(inst.query('CURV?0\n'))
