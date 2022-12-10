import matplotlib.pyplot as plt
import geopandas as gpd

def load_data(department: int):
    """
    Loads the GeoPandas dataset for a specific department
    """
    plt.style.use('default')
    folium_tile = "CartoDB Positron"

    wfs_communes = f"https://wxs.ign.fr/topographie/geoportail/wfs?SERVICE=WFS&VERSION=2.0.0" \
               "&request=GetFeature&OUTPUTFORMAT=application/json&typename=BDTOPO_V3:commune&CQL_FILTER=code_insee_du_departement={department}"
    communes = gpd.read_file(wfs_communes)
    communes.drop(['date_creation', 'date_modification'], axis=1, inplace=True)

    return communes