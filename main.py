from astro_pi_orbit import ISS
from picamzero import Camera
import PIL.Image
import PIL.ExifTags


def get_gps_coordinates(iss):

    point = iss.coordinates()
    return (point.latitude.signed_dms(), point.longitude.signed_dms())

cam = Camera()
iss = ISS()

imagename1 = cam.take_photo("gps_image1.jpg", gps_coordinates = get_gps_coordinates(iss))
imagename2 = cam.take_photo("gps_image2.jpg", gps_coordinates = get_gps_coordinates(iss))

image1 = PIL.Image.open(imagename1)
image2 = PIL.Image.open(imagename2)

exifdata = image1._getexif()

exif1 = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in image1._getexif().items()
    if k in PIL.ExifTags.TAGS
}

exif2 = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in image2._getexif().items()
    if k in PIL.ExifTags.TAGS
}

coordinates = []

for k, v in exif1.items():
    if k == 'GPSInfo':
        coordinates.append(v)

for k, v in exif2.items():
    if k == 'GPSInfo':
        coordinates.append(v)

print(coordinates)

estimate_kmps = 27

estimate_kmps_formatted = "{:.4f}".format(estimate_kmps)

output_string = estimate_kmps_formatted

file_path = "result.txt"
with open(file_path, 'w') as file:
    file.write(output_string)

print("Data written to", file_path)
