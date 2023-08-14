# ECG-and-Heart-Rate-Monitor

This set of programs is designed to allow users to create and visualize an electrocardiogram (ECG) signal using a combination of Arduino hardware and a python script. The Arduino program utilizes the Sparkfun MAX3010x library to gather heart rate data from a sensor attached to the user. This data is then passed to a python script, which uses the numpy library to perform computations on the collected data. The computed data is then plotted using the matplotlib library, resulting in a visual representation of the ECG signal. This graphical representation allows users to observe the ECG signal and study its characteristics, such as the amplitudes and durations of the different waveforms. In addition to the default ECG signal, the program also allows users to customize certain waveform characteristics by inputting their own specifications. This customization feature allows users to experiment with different ECG configurations and observe the resulting changes in the visualized signal. Overall, this set of programs provides a versatile tool for generating and visualizing ECG signals for educational or experimental purposes.

Schematic:
![Schematic](https://i.imgur.com/7FHopCs.png)

Hardware Setup:
![Hardware Setup](https://i.imgur.com/tqrMKiV.png)

Sensor Activation Displaying Heart Rate:
![Hardware Setup](https://imgur.com/a/kxeW60D)

Sample Signal Graph:
![Hardware Setup](https://imgur.com/a/6QPE35g)
