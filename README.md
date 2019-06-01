# Remote-PC-control-with-raspberry-pi-Flask
PC turn on and check status. Using raspberry pi zero w with python Flask web server. 

i will turn on pc through web page.
and check status.

this function is already implemented with wake on lan. but i want to make this with flask web server and raspberry pi zero.


i show structure of this project. 
i will control pc with relay to connect mother board power pin. 
physically turn on 	pc is simple. just connect power pin with conducting material such as screwdriver. 

I made a flask web server using a python file and some html files. flask file make order to another python file ‘turn_on_pc.py’. this file send gpio signal to relay. 
and this web page check pc status by send a ping to pc, once every 200 seconds. 
you can copy and paste these files from my github.


