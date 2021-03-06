from tkinter import Tk, mainloop, TOP, BOTTOM
from tkinter.ttk import Button
import os

root = Tk()
gpu01_status = 'working'

def reboot_linux():

	global gpu01_status
	print("reboot")
	#os.sytem("reboot")

def readGpu_mem_occ():
	global gpu01_status
	#
	f= open("/sys/class/drm/card0/device/pp_mclk_od","r")
	data = str(f.readline())
	data = int(data)
	f= open("/sys/class/drm/card0/device/pp_mclk_od","r")
	data1 = str(f.readline())
	data1 = int(data1)
	print(data)
	print(data1)
	print(data and data1)
	if (data and data1) == 0:
		print("restart in act")
		gpu01_status = 'halt reboot now'
		root.after(10000, reboot_linux())
		return		
	gpu01_status = 'ok'
	root.after(50000,readGpu_mem_occ)


root.after(50000,readGpu_mem_occ)
button_status = Button(root, text = 'GPU0-1 is '+ gpu01_status)

button_status.pack(side = TOP,pady = 30)

root.mainloop()
