# fraction-coeffs
Extracts frictionCoeff.txt file in CityCAT format from a shape file.

## Description
This model takes a shape file with non-default friction coefficients. These have polygons with an assocaited "value" which is the new friction coefficent

## Input Files (data slots)
* friction coefficient
  * Description: A .shp file for the non default friction coefficient. The shape file has a "value" which is the new friction coefficient
  * Location: /data/inputs

## Outputs
The model should output only one file a FrictionCoeffs.txt file
