import math


mu1=0.299
var1=0.05
samples1=150

mu2=0.307
var2=0.08
samples2=165


set1 = { "mu":mu1, "var":var1 , "N":samples1 }
set2 = { "mu":mu2, "var":var2 , "N":samples2 }



t = ( set1['mu'] - set2['mu'] ) / float( math.sqrt((set1['var']/set1['N']) + (set2['var']/set2['N'])))

num = math.pow( (set1['var']/set1['N'] + set2['var']/set2['N']), 2) 

den = float( (math.pow(set1['var'],2) / (math.pow(set1['N'],2)*(set1['N'] -1))) + ( math.pow(set2['var'],2) / (math.pow(set2['N'],2)*(set2['N'] -1))))

v = ( num / den )

print "t: %0.3f" % t
print "v: %0.3f" % v

