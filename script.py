#authors: Fergus Mcclean, Chris Iliadis
#host: Newcastle University
import geopandas as gpd
#from citycatio.utils import geoseries_to_string
import os

def geoseries_with_value_to_string(geoseries: gpd.GeoSeries, value, index=False, index_first=True):
    """GeoSeries to CityCAT string representation

    Args:
        geoseries: Polygons to convert
        value: Fraction coefficient value
        index: Whether or not to include the index
        index_first: Whether or not to place the index before the number of points
    Returns:
        s (str): String representation readable by CityCAT

    """
    assert (geoseries.geom_type == 'Polygon').all(), 'Geometries must be of type Polygon'

    s = '{}\n'.format(len(geoseries))

    for idx, geometry in geoseries.items():
        if not index:
            s += '{}'.format(len(geometry.exterior.coords))
        elif index_first:
            s += '{} {}'.format(idx, len(geometry.exterior.coords))
        else:
            s += '{} {}'.format(len(geometry.exterior.coords), idx)
        s += ' {}'.format(value[idx])
        x, y = geometry.exterior.coords.xy
        for x_val in x:
            s += ' {}'.format(x_val)
        for y_val in y:
            s += ' {}'.format(y_val)
        s += '\n'

    return s

class FrictionCoefficents:
    """Areas representing different friction coefficents

    Args:
        data: Table containing Fraction coefficient polygons

    """
    def __init__(self, data: gpd.GeoDataFrame):
        assert type(data) == gpd.GeoDataFrame
        self.data = data

    def write(self, path):
        with open(os.path.join(path, 'FrictionCoeffs.txt'), 'w') as f:
            f.write(geoseries_with_value_to_string(self.data.geometry,self.data.Value))


# Define Data Paths
data_path = os.getenv('DATA_PATH', '/data')
inputs_path = os.path.join(data_path,'inputs')
#outputs_path = 'outputs/'


name_shp_file = 'FrictionCoeffs-test'

gdf = gpd.read_file(inputs_path + name_shp_file + '.shp')
FrictionCoefficents(gdf).write('.')

# Just printing the output of the file to show what's in it
with open('FrictionCoeffs.txt') as f:
  print(*f.readlines()[:10])
  

