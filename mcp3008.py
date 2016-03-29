#Code credited to Jeremy Blythe at:
#https://github.com/jerbly/Pi/blob/master/mcp3008.py
import spidev

spi = spidev.SpiDev()
#spi.open(0,0)
#^ For some reason this function is not working. Perhaps something is missing from
#The SPI packages

# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
def readadc(adcnum):
    if ((adcnum > 7) or (adcnum < 0)):
        return -1
    r = spi.xfer2([1,(8+adcnum)<<4,0])
    adcout = ((r[1]&3) << 8) + r[2]
    return adcout