from astro_pi_orbit import ISS
from picamzero import Camera
import PIL.Image
from PIL.ExifTags import TAGS, GPSTAGS


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

for tag, value in exifdata.items():
        exif_table = {}
        decoded = TAGS.get(tag, tag)
        exif_table[decoded] = value

gps_info = {}
for key in exif_table['gps_info'].keys():
    decode = GPSTAGS.get(key,key)
    gps_info[decode] = exif_table['gps_info'][key]

print(gps_info)

# exif1 = {
#     PIL.ExifTags.TAGS[k]: v
#     for k, v in image1._getexif().items()
#     if k in PIL.ExifTags.TAGS
# }

# exif2 = {
#     PIL.ExifTags.TAGS[k]: v
#     for k, v in image2._getexif().items()
#     if k in PIL.ExifTags.TAGS
# }

# coordinates = []

# for k, v in exif1.items():
#     if k == 'GPSInfo':
#         v = str(v)
#         coordinates.append(v)

#     print(v)

#     if v:
#         v = str(v)
#         latitude = f"{v[2][0]}°{v[2][1]}'{v[2][2]}\" {v[1]}"
#         longitude = f"{v[4][0]}°{v[4][1]}'{v[4][2]}\" {v[3]}"

# # for k, v in exif2.items():
# #     if k == 'GPSInfo':
# #         coordinates.append(v)


# print(f"{latitude} : {longitude}")
    
estimate_kmps = 27

estimate_kmps_formatted = "{:.4f}".format(estimate_kmps)

output_string = estimate_kmps_formatted

file_path = "result.txt"
with open(file_path, 'w') as file:
    file.write(output_string)

print("Data written to", file_path)
