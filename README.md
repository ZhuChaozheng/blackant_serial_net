# blackant_serial_net
  our lab plan to release our devices which are used in communication field through 4G. By utilizing our devices, you can send/receive data from web to serial. Now, we deceide to release our demo source code to help more people realize the function of ser2net especially ser2web.
  
  it's just like a demo of modscan32 run in the web.

# about client
client_read_send.py: read data from serial and send to web, run it on an equipment connected to a serial device like raspberry
  
client_recv_write.py:read data from web and write to serial, run it on an equipment connected to a serial device like raspberry

ps: you may need to change the address

# start the server

``cd blackant_serial_net\web

export FLASK_APP=manage

export FLASK_ENV=development

flask run``
