from scatter_mapbox_plot import scatter_plot
from trace_plot import trace_plot
from gaussian_blur_plot import gaussian_blur_plot
from heatmap_test import rasterized_heatmap
'''
Setting the boolean to true enables filesaving 
'''

'''To plot, insert the location of the data folder. This should be on the format: Name/Name-yyyymmdd-yyyymmdd'''

'''Brazil plots - 7 days'''
gaussian_blur_plot("Brazil/Brazil-20240912-20240918", False, 1.5)
#trace_plot("Brazil-20240912-20240918", False)

'''Australia plots - 7 days'''  
#gaussian_blur_plot("Australia-20240912-20240918", False, 1.5)
#trace_plot("Australia-20240912-20240918", False)
