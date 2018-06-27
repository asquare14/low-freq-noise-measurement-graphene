from tkinter import *
import applyv_2400
import injecti_2400
import srs760
import measure_noise

def main():
    main_app = Tk()
    main_app.wm_title("Home")
    frame_top = Frame(main_app)
    frame_top.pack()
    frame_bottom = Frame(main_app)
    frame_bottom.pack(side = BOTTOM)

    Getdata_b = Button(frame_top, text = "Start Noise Measurements", command = measure_noise.start_noise_measurements, bg = "ivory")
    Exit_b = Button(frame_bottom, text = "Close", command = main_app.destroy, bg = "ivory")
    Getdata_b.flash()
    Exit_b.flash()
    Getdata_b.pack(side = LEFT)
    Exit_b.pack(side = BOTTOM)

    main_app.mainloop()

if __name__ == '__main__':
    main()
