import rasterio as rio

def get_area(postal_code):
    global df

    area_of_interest = df.loc[df.code_insee == postal_code]
    area_of_interest.plot()

    # check bounds formatting
    bbox = tuple(area_of_interest.bounds.values[0])
    assert bbox == rio.features.bounds(area_of_interest), "Bounds format is incorrect"

    polygons = list(area_of_interest.geometry.values[0])
    polygons = sorted(polygons, key=lambda poly: poly.area, reverse=True)
    polygons[0]

    roi = polygons[0]
    bbox = roi.bounds

    return area_of_interest, roi, bbox