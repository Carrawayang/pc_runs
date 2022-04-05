import re
import matplotlib.pyplot as plt
import numpy as np
f = open("./wR2_.txt")
byt = f.readlines()
time = []
loss = []
for i in byt:
    time.append(re.findall(r"\d+\.?\d*",i)[1])
    loss.append(re.findall(r"\d+\.?\d*",i)[2])

f.close()
f = open("./2_.txt","w+")
for i in loss :
    f.write(i+"\n")   
f.close()
t = []
t.append(0)
tag = 0
for i in range(len(time)):
    tag= tag + float(time[i])
    t.append(tag)
t.pop()
f = open("./1_.txt","w+")
for i in t :
    f.write(str(i)+"\n")
