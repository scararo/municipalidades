
g = open('mun_dec_2.txt', 'w')


with open('municipalidades.txt', 'r') as f:

    for line in f.readlines():
    
        line = line.replace('\t','')
        line = line.replace('\n','')
        l = line.split(',')

        nombre = l[0].strip()
        provincia = l[1].strip()
        region = l[2].strip()

        latitud = l[3]
        longitud = l[4]

        lat_g = latitud.split('°')[0]
        lat_m = latitud.split('°')[1].split('\'')[0]
        lat_s = latitud.split('°')[1].split('\'')[1].split('"')[0]

        lat_g = float(lat_g) 
        lat_m = float(lat_m)
        lat_s = float(lat_s)

        if lat_g > 0: 
            lat_dd = round(lat_g + lat_m/60. + lat_s/3600.,4)
        else:
            lat_dd = round(lat_g - lat_m/60. - lat_s/3600.,4)

        lon_g = longitud.split('°')[0]
        lon_m = longitud.split('°')[1].split('\'')[0]
        lon_s = longitud.split('°')[1].split('\'')[1].split('"')[0]

        lon_g = float(lon_g) 
        lon_m = float(lon_m)
        lon_s = float(lon_s)

        if lon_g > 0:
            lon_dd = round(lon_g + lon_m/60. + lon_s/3600.,4)
        else:
            lon_dd = round(lon_g - lon_m/60. - lon_s/3600.,4)
            
        linea = '{}, {}, {}, {}\n'.format(region, nombre, lat_dd, lon_dd)
        print(linea)
        g.write(linea)

g.close()
