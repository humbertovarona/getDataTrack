def read_drifterData(file_path):
    with Dataset(file_path, 'r') as nc_file:
        time = nc_file.variables['time'][:]
        time_units = nc_file.variables['time'].units
        #time_calendar = time.calendar
        #ntime = np.asarray(time, dtype='datetime64[' + time_units + ']')
        longitude = nc_file.variables['lon'][:]
        latitude = nc_file.variables['lat'][:]
        uc = nc_file.variables['uc'][:]
        vc = nc_file.variables['vc'][:]
        drifter_id = nc_file.getncattr("Drifter_ID")
    return time, longitude, latitude, uc, vc, drifter_id
