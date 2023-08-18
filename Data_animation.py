import os
import numpy as np
import matplotlib.animation as ani
from matplotlib import pyplot as plt
import pandas as pd

# f_datapath = "/home/srdream/WORK/Recover/RV_to_eta_to_c/Eta_Psi/"
# file_name = "Eta_Psi_{}.dat"

f_datapath = "/home/srdream/WORK/Recover/RV_to_eta_to_c/Cx/"
file_name = "Cx_{}.dat"


def extract_data(file_number):
    f_name = file_name.format(file_number)
    full_name = f"{f_datapath}{f_name}"
    if os.path.isfile(full_name) is False:
        print("Cannot open the file")
        exit(0)
    data_frame = pd.read_csv(full_name, sep='\t', header=1, names=('1', '2', '3'))
    #data_frame = pd.read_csv(full_name, sep='\t', header=0, names=('1', '2'))

    return data_frame


def animation(i):
    file_df = extract_data(i + 1)
    x = file_df['1']
    y = file_df['2']
    z = file_df['3']
    line.set_data(x, np.sqrt(y * y + z * z))
    line1.set_data(x, np.sqrt(y * y + z * z))
    #line.set_data(x, y)

   # line1.set_data(x, y)

    dt = i * 100
    plt.suptitle(t=f"t = {dt} s.")
    #return line
    return line,line1


fig = plt.figure(figsize=(10, 6))
axes: fig = plt.axes(xlim=(0.0, 1256.0), ylim=(-0.0, 0.1))
plt.grid(ls='--', color='black')
axes1: fig = plt.axes([.625,.595,.25,.25],xlim=(600, 650), ylim=(0.05, 0.08))
plt.grid(ls='--', color='black')
#axes: fig = plt.axes(xlim=(-0, 2048.0), ylim=(1e-16, 0.05)) # ylim has to be non-zero for log scale!
#plt.grid(ls='--', color='black')
axes.set(title='The Envelope of Single Breather in RV-equations', xlabel='x, [km]', ylabel='|Psi(x)|')
axes1.set(title='zoomed')
#axes.set(title='The Spectrum Eta(k) of Single Breather in RV-equations', xlabel='k', ylabel='eta(k)')
#axes.set_yscale('log')
line, = axes.plot([], [], lw=3)
line1, = axes1.plot([], [], lw=3)


N = len(os.listdir(f_datapath))
film = ani.FuncAnimation(fig, animation, N, interval=100, repeat=False)
Writer = ani.FFMpegWriter(fps=10)
#plt.show()
film.save("SB_in_RV_Psix.mp4", writer=Writer, dpi=100)