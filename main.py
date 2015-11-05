from __future__ import division

m = input("Mass: ")
angle = input("Angle: ")
torquer = 0.012
torque = m*9.81*torquer
print "Torque: %s" %torque
kappa = torque/angle
print "Kappa: %s" %kappa

