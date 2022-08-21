
from Adafruit_IO import RequestError, Client, Feed #Se importa la libreria de Adafruit
from pylab import *

ADAFRUIT_IO_USERNAME = "SammusDeVennus"


ADAFRUIT_IO_KEY = "xxxxxxxxxxxxxxxxxx"



aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try:
    test1 = aio.feeds("senoidal")
    test2 = aio.feeds("cosenoidal")
except RequestError: #En caso de no existir el Feed se crean, en este caso se crearon dos feeds
        test_feed1 =Feed(name="senoidal")
        test_feed1 =aio.create_feed(test_feed1)
        
        test_feed2 =Feed(name="cosenoidal")
        test_feed2 =aio.create_feed(test_feed2)


grados=1

while grados<=360:
    m=sin(grados)
    n=cos(grados)
    aio.send_data(test1.key, m)
    aio.send_data(test2.key, n)
    grados=grados+0.25
    time.sleep(5)
    
    
    
