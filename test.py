import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from autorank import autorank, create_report, plot_stats

data = pd.read_csv('/home/rodolfoviegas/projetos/critical_distance_diagram/crit_dist/rmse.csv')
res = autorank(data, alpha=0.05, verbose=False, order='ascending')
print(res)
report = create_report(res)
report
plot_stats(res)
plt.show()