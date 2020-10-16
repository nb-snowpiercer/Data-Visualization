import turtle
import time
if __name__=="__main__":
	t = turtle.Pen();
	t.pencolor('red');
	for i in range(0,360,3):
		t.seth(i);
		for j in range(4):
			t.fd(100);
			t.left(90);
	time.sleep(3);