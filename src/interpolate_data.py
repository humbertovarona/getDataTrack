def interpolate_data(longitude, latitude, data, target_longitude, target_latitude):
    lon_mesh, lat_mesh = np.meshgrid(longitude, latitude)
    target_points = np.column_stack((target_longitude, target_latitude))
    interpolated_data = griddata((lon_mesh.flatten(), lat_mesh.flatten()), data.flatten(), target_points)
    interpolated_data = np.reshape(interpolated_data, target_longitude.shape)
    return interpolated_data
