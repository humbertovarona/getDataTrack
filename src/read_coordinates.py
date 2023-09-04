def read_coordinates(file_path, variablesList):
    with Dataset(file_path, 'r') as nc_file:
        longitude = nc_file.variables[variablesList[0]][:]
        latitude = nc_file.variables[variablesList[1]][:]
    return longitude, latitude
  
