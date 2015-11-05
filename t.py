from __future__ import division
import math

kappa = input("Kappa: ")
I = input("I: ")

T = 2*math.pi*math.sqrt(I/kappa)
print "Tcalc: %s" %T