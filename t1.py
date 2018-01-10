import numpy as np
import random
from scipy.io.wavfile import write
import pickle
import sounddevice as sd
n=44100*random.randint(5,31)
a=np.zeros((n,2))
for i in range(n):
    a[i,0]=random.randint(0,65536)
    a[i,1]=random.randint(0,65536)
print(a)
pickle_out=open("a.pkl","wb")
pickle.dump(a,pickle_out)
pickle_out.close()
scale=np.int16(a/np.max(np.abs(a)) * 32767)
write('a.wav',44100,scale)



