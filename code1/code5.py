import turtle
import time
if __name__=="__main__":
	t = turtle.Pen()
	t.shape('turtle')
	t.fillcolor('red')
	t.pencolor('red')
	t.seth(36);
	t.begin_fill()
	t.fd(200)
	t.left(144)
	t.fd(200)
	t.left(144)
	t.fd(200)
	t.left(144)
	t.fd(200)
	t.left(144)
	t.fd(200)
	t.left(144)
	t.end_fill();
	t.hideturtle();
	time.sleep(3)