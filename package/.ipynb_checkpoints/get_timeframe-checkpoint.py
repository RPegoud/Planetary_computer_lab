import pystac_client
import planetary_computer
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


def get_timeframe(time_of_interest: str, bbox):

    catalog = pystac_client.Client.open(
        "https://planetarycomputer.microsoft.com/api/stac/v1",
        modifier=planetary_computer.sign_inplace,
    )

    # Searching for S2-L2 products within ROI and time range
    search = catalog.search(
        collections=["sentinel-2-l2a"],
        bbox=bbox,  # or intersects=area_of_interest
        datetime=time_of_interest,
        sortby='datetime',  # By default the query returns latest first, here we sortby ascending
        query={"eo:cloud_cover": {"lt": 10}},  # cloud cover lower than 10%
    )
    items = search.item_collection()
    print(f"Found {len(items)} items\n")
    
    gdf_items = gpd.GeoDataFrame.from_features(items.to_dict(), crs="epsg:4326")
    
    gdf_items["datetime"] = pd.to_datetime(gdf_items.datetime)
    
    fig, ax = plt.subplots(figsize=(10,2))
    plt.scatter(gdf_items.datetime, gdf_items["eo:cloud_cover"])
    ax.set_ylabel("Cloud cover (%)")
    
    return gdf_items