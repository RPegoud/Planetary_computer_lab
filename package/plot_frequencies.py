import pystac
import rasterio as rio
import rasterio.plot, rasterio.features, rasterio.mask, rasterio.fill  # Not loaded by default
import matplotlib.pyplot as plt
import rich.table

def plot_frequencies(before: pystac.item.Item, after: pystac.item.Item, bbox: tuple):
    with rio.open(before.assets["visual"].href) as ds:
        profile = ds.profile
        rich.print(profile)
        crs = profile['crs']
        warped_aoi_bounds = rio.warp.transform_bounds("epsg:4326", crs, *bbox)
        aoi_window = rio.windows.from_bounds(*warped_aoi_bounds, transform=profile["transform"])
        aoi_window = aoi_window.round_shape().round_offsets()
        with rio.open(before.assets["visual"].href) as ds:
            viz_before = ds.read(window=aoi_window)
        with rio.open(after.assets["visual"].href) as ds:
            viz_after = ds.read(window=aoi_window)
        print("bands: {}, rows: {}, cols: {}\n".format(*viz_before.shape) + f"dtype: {viz_before.dtype}")

        fig, ax = plt.subplots(figsize=(10,4))
        rio.plot.show_hist(viz_before, bins=64, stacked=False, alpha=0.5, title="Histogram")

        return crs, aoi_window, viz_before, viz_after