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
