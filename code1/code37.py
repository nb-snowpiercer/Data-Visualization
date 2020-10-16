import turtle
import time
if __name__=="__main__":
	t = turtle.Pen();
	t.pencolor('red');
	i = 0
	while i<360:
		t.seth(i);
		j = 0;
		while j<4:
			t.fd(100);
			t.left(90);
			j+=1; 
		i+=3;
	time.sleep(3);