import turtle
import time
if __name__=="__main__":
	t = turtle.Pen();
	t.shape('turtle');
	t.fillcolor('orange');
	t.pencolor('blue');
	t.begin_fill();
	t.fd(100);
	t.left(90);
	t.fd(100);
	t.left(90);
	t.fd(100);
	t.left(90);
	t.fd(100);
	t.end_fill();
	t.fillcolor('blue');
	t.begin_fill()
	t.fd(100);
	t.left(90);
	t.fd(100);
	t.left(90);
	t.fd(100);
	t.left(90);
	t.fd(100);
	t.end_fill()
	t.fillcolor('red');
	t.begin_fill()
	t.fd(100);
	t.left(90);
	t.fd(100);
	t.left(90);
	t.fd(100);
	t.left(90);
	t.fd(100);
	t.end_fill()
	t.fillcolor('green');
	t.begin_fill()
	t.fd(100);
	t.left(90);
	t.fd(100);
	t.left(90);
	t.fd(100);
	t.left(90);
	t.fd(100);
	t.end_fill()
	t.hideturtle()
	time.sleep(3)