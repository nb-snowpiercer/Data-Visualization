import turtle
import time
if __name__=="__main__":
	t = turtle.Pen();
	t.color('red');
	i = 0
	while i<360:
		t.seth(i);
		t.circle(100);
		i+=15;
	time.sleep(3);