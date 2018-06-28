from tkinter import *
import measure_noise
import measure_voltage
import nanovoltmeter

def main():
    main_app = Tk()
    main_app.wm_title("Home")
    frame_top = Frame(main_app)
    frame_top.pack()
    frame_bottom = Frame(main_app)
    frame_bottom.pack(side = BOTTOM)
    Getnoisedata_b = Button(frame_top, text = "Start Noise Measurements", command = measure_noise.start_noise_measurements, bg = "ivory")
    Getvoltagedata_b = Button(frame_top, text = "Start Voltage Measurements", command = measure_voltage.start_voltage_measurements, bg = "ivory")
    Exit_b = Button(frame_bottom, text = "Close", command = main_app.destroy, bg = "ivory")
    Getnoisedata_b.flash()
    Getvoltagedata_b.flash()
    Exit_b.flash()
    Getnoisedata_b.pack(side = LEFT)
    Getvoltagedata_b.pack(side = LEFT)
    Exit_b.pack(side = BOTTOM)
    main_app.mainloop()

if __name__ == '__main__':
    main()
