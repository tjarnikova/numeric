filelist = 'ice/icec.day.mean.2014.v2.nc'
with Dataset(filelist) as nc:
    #print(nc.variables)
    icec=nc.variables['icec'][...]
    lat =nc.variables['lat'][...] 
    lon = nc.variables['lon'][...]
    time = nc.variables['time'][...]

#dealing with the mask in icec - assuming it's a value of 0
#figuring out how to make this mask took me a solid frustrating half-hour

w = icec[0,0,0]


le_mask = np.ma.getmask(icec)
icec[le_mask]=0