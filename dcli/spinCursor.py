import threading
import sys, os
import time
import unicodedata

#from http://code.activestate.com/recipes/534142-spin-cursor/
class SpinCursor(threading.Thread):
    """ A console spin cursor class """
    
    def __init__(self, msg='', maxspin=0, minspin=10, speed=5, longTimeAfter=5):
        # Count of a spin
        self.count = 0
        self.out = sys.stdout
        self.flag = False
        self.max = maxspin
        self.min = minspin
        self.since = 0
        self.longTimeAfter = longTimeAfter
        # Any message to print first ?
        self.msg = msg
        # Complete printed string
        self.string = ''
        # Speed is given as number of spins a second
        # Use it to calculate spin wait time
        self.waittime = 1.0/float(speed*4)
        if os.name == 'posix':
            self.spinchars = (unicodedata.lookup('FIGURE DASH'),u'\\ ',u'| ',u'/ ')
        else:
            # The unicode dash character does not show
            # up properly in Windows console.
            self.spinchars = (u'-',u'\\ ',u'| ',u'/ ')        
        threading.Thread.__init__(self, None, None, "Spin Thread")
        
    def spin(self):
        """ Perform a single spin """

        for x in self.spinchars:
            self.string = self.msg + "...\t" + x + "\r"
            if (time.time() - self.since > self.longTimeAfter):
                if (time.time() - self.since > self.longTimeAfter * 6):
                    self.string = '🐌🐌 Internet seems to be very slow..' + self.string
                elif (time.time() - self.since > self.longTimeAfter * 4):
                    self.string = '🐌 Internet seems to be slow..' + self.string
                else:
                    self.string = 'First time may take time.' + self.string
            self.out.write(self.string)
            self.out.flush()
            time.sleep(self.waittime)

    def run(self):
        self.since = time.time()
        while (not self.flag) and ((self.count<self.min) or (self.count<self.max)):
            self.spin()
            self.count += 1

        # Clean up display...
        self.out.write(" "*(len(self.string) + 1))
        
    def stop(self):
        self.flag = True
        