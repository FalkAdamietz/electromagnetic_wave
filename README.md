# electromagnetic_wave
 Simulation of an electromagnetic wave.
 ![Example animation](https://github.com/Bra-A-Ket/electromagnetic_wave/blob/main/em_wave.gif)
 ## Required packages
 1. Numpy:
 ```bash
 python -m pip install numpy
 ```
 2. matplotlib:
 ```bash
 python -m pip install matplotlib
 ```
 3. tqdm
 ```bash
 python -m pip install tqdm
 ```
 ## Usage
 - Choose e.g.
 ```python
 k = 0.07 #abs(wave vector)
 omega = 0.2 #angular frequency = 2*pi/T
 dt = 0.1 #time step
 max = 100 #maximum length of axis
 amp = 100 #(scaled) amplitude of the waves
 ```
 and let the script to the rest
 ## Execution
 The python script em_wave.py has to be executed in the main directory like
 ```bash
 python -m em_wave
 ```
