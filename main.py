import libarchive.public
import libarchive.constants

def writer(buffer_, length):
    d += buffer_
    return length
for entry in libarchive.public.create_generic(writer,format_name=libarchive.constants.ARCHIVE_FORMAT_7ZIP,files=['curld/']):
    print(entry)
print data
