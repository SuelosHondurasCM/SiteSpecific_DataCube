import spatialdata
import numpy as np
from spatialdata.gis_functions import masking_rescaling_xrdata, add_2dlayer_toxarrayr
from spatialdata.datacube import create_dimension
from spatialdata.soil_data import find_soil_textural_class_in_nparray
from .process import get_crs_fromxarray