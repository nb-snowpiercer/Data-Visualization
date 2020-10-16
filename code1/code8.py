import turtle
import time
if __name__=="__main__":
	t = turtle.Pen();
	t.color('red');
	for i in range(0,360,15):
		t.seth(i);
		t.circle(100);
	time.sleep(3);