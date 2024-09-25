import gpsd

# Connect to the local gpsd
gpsd.connect()

# Main loop
try:
    while True:
        packet = gpsd.get_current()
        print('Latitude:', packet.lat)
        print('Longitude:', packet.lon)
        print('Altitude:', packet.alt)
except KeyboardInterrupt:
    print('\nExiting...')
