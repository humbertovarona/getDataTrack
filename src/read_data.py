def read_data(file_path, variablesList):
    with Dataset(file_path, 'r') as nc_file:
        longitude = nc_file.variables[variablesList[0]][:]
        latitude = nc_file.variables[variablesList[1]][:]
        time = nc_file.variables[variablesList[2]][:]
        variable = nc_file.variables[variablesList[3]][:]
    return longitude, latitude, time, variable
