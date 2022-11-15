import matplotlib.pyplot as plt
import numpy as np
 
# Generate time values for the signal
x = np.arange(0.01, 2.01, 0.01)
 
default = int(input('Press 1 if u want default ecg signal else press 2:\n'))
if default == 1:
   li = 30/72
   a_pwav = 0.25
   d_pwav = 0.09
   t_pwav = 0.16
   a_qwav = 0.025
   d_qwav = 0.066
   t_qwav = 0.166
   a_qrswav = 1.6
   d_qrswav = 0.11
   a_swav = 0.25
   d_swav = 0.066
   t_swav = 0.09
   a_twav = 0.35
   d_twav = 0.142
   t_twav = 0.2
   a_uwav = 0.035
   d_uwav = 0.0476
   t_uwav = 0.433
else:
   rate = int(input('\n\nenter the heart beat rate :'))
   li = 30/rate
   # p wave specifications
   print('\n\np wave specifications\n')
   d = int(input('Enter 1 for default specification else press 2: \n'))
   if d == 1:
       a_pwav = 0.25
       d_pwav = 0.09
       t_pwav = 0.16
   else:
       a_pwav = float(input('amplitude = '))
       d_pwav = float(input('duration = '))
       t_pwav = float(input('p-r interval = '))
       d = 0
 # q wave specifications
   print('\n\nq wave specifications\n')
   d = int(input('Enter 1 for default specification else press 2: \n'))
   if d == 1:
       a_qwav = 0.025
       d_qwav = 0.066
       t_qwav = 0.166
   else:
       a_qwav = float(input('amplitude = '))
       d_qwav = float(input('duration = '))
       t_qwav = 0.1
       d = 0
   # qrs wave specifications
   print('\n\nqrs wave specifications\n')
   d = int(input('Enter 1 for default specification else press 2: \n'))
   if d == 1:
       a_qrswav = 1.6
       d_qrswav = 0.11
   else:
       a_qrswav = float(input('amplitude = '))
       d_qrswav = float(input('duration = '))
       d = 0
   # s wave specifications
   print('\n\ns wave specifications\n')
   d = int(input('Enter 1 for default specification else press 2: \n'))
   if d == 1:
       a_swav = 0.25
       d_swav = 0.066
       t_swav = 0.125
   else:
       a_swav = float(input('amplitude = '))
       d_swav = float(input('duration = '))
       t_swav = 0.125
       d = 0
   # t wave specifications
   print('\n\nt wave specifications\n')
   d = int(input('Enter 1 for default specification else press 2: \n'))
   if d == 1:
       a_twav = 0.35
       d_twav = 0.142
       t_twav = 0.18
   else:
       a_twav = float(input('amplitude = '))
       d_twav = float(input('duration = '))
       t_twav = float(input('s-t interval = '))
       d = 0
   # u wave specifications
   print('\n\nu wave specifications\n')
   d = int(input('Enter 1 for default specification else press 2: '))
   if d == 1:
       a_uwav = 0.035
       d_uwav = 0.0476
       t_uwav = 0.433
   else:
       a_uwav = float(input('amplitude = '))
       d_uwav = float(input('duration = '))
       t_uwav = 0.433
 
def p_wav(x, a, d, t, li):
   l = 1
   x = x + (1/1.8)
   b = 3
   n = 100
   p1 = 1/l
   p2 = 0
   for i in range(1, n+1):
       harm1 = (((np.sin((np.pi/(2*b))*(b-(2*i))))/(b-(2*i))+(np.sin((np.pi/(2*b))*(b+(2*i))))/(b+(2*i)))*(2/np.pi))*np.cos((i*np.pi*x)/l)
       p2 = p2 + harm1
   pwav1 = p1 + p2
   pwav = a * pwav1
   return pwav
 
def q_wav(x, a, d, t, li):
   l = 1
   x = x + l/6
   b = 15
   n = 100
   q1 = (a/(2*b))*(2-b)
   q2 = 0
   for i in range(1, n+1):
       harm5 = (((2*b*a)/(i*i*np.pi*np.pi))*(1-np.cos((i*np.pi)/b)))*np.cos((i*np.pi*x)/l)
       q2 = q2 + harm5
   qwav = -1*(q1 + q2)
   return qwav
 
def qrs_wav(x, a, d, li):
   l = 1
   b = 5
   n = 100
   qrs1 = (a/(2*b))*(2-b)
   qrs2 = 0
   for i in range(1, n+1):
       harm = (((2*b*a)/(i*i*np.pi*np.pi))*(1-np.cos((i*np.pi)/b)))*np.cos((i*np.pi*x)/l)
       qrs2 = qrs2 + harm
   qrswav = qrs1 + qrs2
   return qrswav
 
def s_wav(x, a, d, t, li):
   l = 1
   x = x - l/6
   b = 15
   n = 100
   s1 = (a/(2*b))*(2-b)
   s2 = 0
   for i in range(1, n+1):
       harm3 = (((2*b*a)/(i*i*np.pi*np.pi))*(1-np.cos((i*np.pi)/b)))*np.cos((i*np.pi*x)/l)
       s2 = s2 + harm3
   swav = -1*(s1 + s2)
   return swav
 
def t_wav(x, a, d, t, li):
   l = 1
   a = 0.35
   x = x - (1/1.8)
   b = 7
   n = 20
   t1 = 1/l
   t2 = 0
   for i in range(1, n+1):
       harm2 = (((np.sin((np.pi/(2*b))*(b-(2*i))))/(b-(2*i))+(np.sin((np.pi/(2*b))*(b+(2*i))))/(b+(2*i)))*(2/np.pi))*np.cos((i*np.pi*x)/l)
       t2 = t2 + harm2
   twav1 = t1 + t2
   twav = a * twav1
   return twav
 
def u_wav(x, a, d, t, li):
   l = 1
   a = 0.03
   x = x - (1/1.1)
   b = 21
   n = 100
   u1 = 1/l
   u2 = 0
   for i in range(1, n+1):
       harm4 = (((np.sin((np.pi/(2*b))*(b-(2*i))))/(b-(2*i))+(np.sin((np.pi/(2*b))*(b+(2*i))))/(b+(2*i)))*(2/np.pi))*np.cos((i*np.pi*x)/l)
       u2 = u2 + harm4
   uwav1 = u1 + u2
   uwav = a * uwav1
   return uwav
 
 
