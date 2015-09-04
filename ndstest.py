import nds2

conn = nds2.connection('nds.ligo-la.caltech.edu')
print conn
channel = ['L1:IOP-SUS_AUX_H56_DAC_DT_OUT_DQ']
print "channel = {0}".format(channel)

print "Now testing the command 'conn.iterate(channel)' "

try:
    iter = conn.iterate(channel)
except RuntimeError, err:
    print "Failed"
    print RuntimeError, err


print "Now testing the command 'conn.iterate(1, channel)' "

try:
    iter = conn.iterate(1, channel)
except RuntimeError, err:
    print "Failed"
    print RuntimeError, err

print "Now testing the command 'conn.iterate(1125417950, 1125418050, channel)' "

try:
    iter = conn.iterate(1125417950, 1125418050, channel)
except RuntimeError, err:
    print "Failed"
    print RuntimeError, err

print "Now testing the command 'conn.iterate(1125417950, 1125418050, 1, channel)' "

try:
    iter = conn.iterate(1125417950, 1125418050, 1, channel)
except RuntimeError, err:
    print "Failed"
    print RuntimeError, err