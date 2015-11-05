from __future__ import division

M = input("Mass of disk: ")
rinner = input("Inner radius of disk: ")
router = input("Outer radius of disk: ")

I = M/2*(rinner*rinner + router*router)
print "IDisk: %s" %I
