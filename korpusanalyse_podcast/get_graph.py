# # libraries & dataset
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

input_path = "results/changes_per_month.csv"
data = pd.read_csv(input_path, parse_dates=True, index_col=0)
data.columns=["change"]

my_color=np.where(data.index=="2020-04-08", 'orange', 'skyblue')

(markers, stemlines, baseline)= plt.stem(data.index, data["change"])

plt.setp(markers, marker='D', markersize=5, markeredgecolor="orange", markeredgewidth=1)
#plt.setp(baseline, linestyle="-", color=my_color, linewidth=2)
plt.setp(stemlines, linestyle="-", color="olive", linewidth=0.5)
plt.xlabel="Datum"
plt.ylabel="Veränderung (in %)"
plt.title="Veränderung der Häufigkeit der Top-Ten-Wörter der Podcastfolge im DLF-Korpus unmittelbar vor und nach der Veröffentlichung"
# plt.set(xlabel="Datum",
#        ylabel="Veränderung (in %)",
#        title="Veränderung der Häufigkeit der Top-Ten-Wörter der Podcastfolge im DLF-Korpus unmittelbar vor und nach der Veröffentlichung",)
plt.show()
