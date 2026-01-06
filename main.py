# from picamzero import Camera

# cam = Camera()

# cam.capture_sequence("sequence", num_images=3, interval=3)

from astro_pi_orbit import ISS
from picamzero import Camera

iss = ISS()

def get_gps_coordinates(iss):
    """
    Returns a tuple of latitude and longitude coordinates expressed
    in signed degrees minutes seconds.
    """
    point = iss.coordinates()
    return (point.latitude.signed_dms(), point.longitude.signed_dms())

cam = Camera()
cam.take_photo("gps_image1.jpg", gps_coordinates=get_gps_coordinates(iss))




estimate_kmps = 7.1234567890  # Replace with your estimate

estimate_kmps_formatted = "{:.4f}".format(estimate_kmps)

output_string = estimate_kmps_formatted

file_path = "result.txt"
with open(file_path, 'w') as file:
    file.write(output_string)

print("Data written to", file_path)
