import tkinter as tk
import numpy as np
import threading

def paint_pixel(x: float, y: float, color: str):
	canvas.create_rectangle(x + 2, 500 - y, x + 2, 500 - y, fill="#"+color, outline="")

def rgbToHex(r,g,b) -> str:
	return '%02x%02x%02x' % (r,g,b)

def coloor( x ) -> str:
	m = int(256 * abs(np.sin(x/50)))
	n = int(256 * abs(np.cos(x/50 + 1)))
	color = rgbToHex(m, n, 240)
	return color

def graph():
	for x in range(0,9009):
		x = x/9
		b = x/10
		y = 45 * pow(b, 4) + 65 * pow(x, 3) +85 * pow(x, 2) + 105 * x -12
		y = y/100000000

		paint_pixel(x-4, y, rgbToHex(233,42,120))

def animate():
	while True:
		graph()
		canvas.delete("all")
		canvas.create_rectangle(3, 3, 1000, 500, fill="black")

if __name__ == '__main__':
	root = tk.Tk()
	root.geometry("1010x510")
	root.resizable(False, False)
	canvas = tk.Canvas(root, width=1000, height=500, bg="black")
	canvas.pack()

	t1 = threading.Thread(target=animate)
	t1.start()

	root.mainloop()