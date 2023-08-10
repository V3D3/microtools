from matplotlib import pyplot as plt
from matplotlib.widgets import Slider
from scipy.interpolate import interp1d as spline
import numpy as np

x = ''
with open ('my_data.txt', 'r') as f:
    x = f.readlines ()

x = ''.join (x).split ('\n\n\n')

db = {}
for line in x:
    line = line.split ('\n')
    id = int (line[0])
    wpm = line[1]
    acc = line[2]
    date = line[-1]
    db[id] = {'wpm':wpm, 'acc':acc, 'date':date}

wpmarr = []
accarr = []
datearr = []

def wpmstoi (w):
    return int (w.split (' ')[0])
def accstoi (a):
    return float (a[:-1])

for k in db:
    wpmarr.append (wpmstoi (db[k]['wpm']))
    accarr.append (accstoi (db[k]['acc']))
    datearr.append (db[k]['date'])

wpmarr = list (reversed (wpmarr))
accarr = list (reversed (accarr))
datearr = list (reversed (datearr))

K = 25
wpm_filtered = np.convolve (np.array (wpmarr), np.ones (K) / K, mode='valid')
# wpm_filtered = np.average (np.array (wpmarr).reshape (-1, K), axis=1)
acc_filtered = np.convolve (np.array (accarr), np.ones (K) / K, mode='valid')
# acc_filtered = np.average (np.array (accarr).reshape (-1, K), axis=1)
# dates_filtered = datearr#[K:]
dates_filtered = range (len (wpm_filtered))

f, ax = plt.subplots ()

f.set_figheight (8)
f.set_figwidth (16)
ax.plot (dates_filtered, wpm_filtered)
ax.plot (dates_filtered, acc_filtered)
# for x in x_vals: ax.annotate (dates_filtered, (x, wpm_filtered[x]))
plt.show ()
