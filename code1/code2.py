import turtle
import time
if __name__=="__main__":
	t = turtle.Pen()
	t.shape('turtle')
	t.pencolor('red')
	t.fillcolor('orange')
	t.begin_fill()
	t.fd(100)
	t.left(120)
	t.fd(100)
	t.left(120)
	t.fd(100)
	t.end_fill()
	time.sleep(3)