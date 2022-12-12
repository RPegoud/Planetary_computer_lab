import matplotlib.pyplot as plt
from rasterio.windows import Window
import rasterio 

def plot_filter(state) : 
    aoi_window = Window(col_off=10000, row_off=5100, width=1000, height=1000)
    with rasterio.open(state.assets['B08'].href) as ds:
        profile = ds.profile
        mask = ds.read_masks(window=aoi_window)
        data = ds.read(window=aoi_window)
    return plt.imshow(data[0])

def plot_filter_magma(state) : 
    aoi_window = Window(col_off=10000, row_off=5100, width=1000, height=1000)
    with rasterio.open(state.assets['B08'].href) as ds:
        profile = ds.profile
        mask = ds.read_masks(window=aoi_window)
        data = ds.read(window=aoi_window)
    return plt.imshow(data[0], cmap="magma", interpolation="bilinear")