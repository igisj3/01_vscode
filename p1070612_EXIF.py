import exifread
import datetime
# Open image file for reading (binary mode)
path_name ='C:\\Users\J4\\Desktop\\1\\DSC_0033.JPG'
f = open(path_name, 'rb')
# Return Exif tags
tags = exifread.process_file(f)
GPS = str(tags['GPS GPSLatitude']).strip().strip('[]')
G1 = GPS.split(',')[0]
G2 = GPS.split(',')[1]
G3 = GPS.split(',')[2]
G31 = G3.split('/')[0]
G32 = G3.split('/')[1]
G33 = float(G31)/float(G32)
ALT = str(tags['GPS GPSAltitude']).strip()
img_date = str(tags['EXIF DateTimeDigitized']).split(' ')[0].replace(':','-')
img_time = str(tags['EXIF DateTimeDigitized']).split(' ')[1]
img_timeAP = datetime.datetime.strptime(img_time,"%H:%M:%S").strftime('%I:%M %p')
#G1 = str(tags['GPS GPSLatitude']).split(',')[0]
#G2 = str(tags['GPS GPSLatitude']).split(',')[1]
#G3 = str(tags['GPS GPSLatitude']).split()[2]

#focal = str(tags['EXIF FocalLength']).strip().strip('/')[0]
f1 = str(tags['EXIF FocalLength']).split('/')[0]
f2 = str(tags['EXIF FocalLength']).split('/')[1]
print(str(tags['EXIF FocalLength']).strip())
print(f1)
print(f2)
focal = float(f1)/float(f2)
print(focal)


#print(float(G1))
#print(float(G2))
#print(float(G33))
#print(float(ALT))
#print(img_date)
#print(img_time)
#print(img_timeAP)
#for tag in tags.keys():
#    if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
#        print ("Key: %s, value %s" % (tag, tags[tag]))

