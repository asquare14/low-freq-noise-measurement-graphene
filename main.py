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

f2 = open("xaxis.txt","w+")
for i in range(399):
    f2.write(inst.query('BVAL?0,'+str(i)+'\n'))
f2.close()


#set frequency range

