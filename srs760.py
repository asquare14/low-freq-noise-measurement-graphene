from Tkinter import *
import tkMessageBox
import visa
import csv
import re

rm = visa.ResourceManager()
inst = rm.open_resource('GPIB0::10::INSTR')

def identify_instrument():
    inst_details = inst.query('*IDN?\n')
    tkMessageBox.showinfo("Instrument Details", inst_details )

def measure():
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
    convert_to_csv()

def convert_to_csv():
        f = open('yaxis.txt', 'r+')
        n = f.read().replace(',','')
        f.truncate(0)
        f.close()

        f = open('yaxis.txt','w+')
        f.write(n)
        f.close()

        myData = [["yaxis", "xaxis"]]
        fy = open("yaxis.txt","r")
        fx = open("xaxis.txt","r")
        y = fy.read().splitlines()
        x = fx.read().splitlines()

        for i in range(len(x)) :
            l = [y[i],x[i]]
            myData.append(l)
        myFile = open('Values.csv','w')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(myData)
        tkMessageBox.showinfo("Done", "Your CSV file 'Values.csv' is ready !" )
