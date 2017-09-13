import optparse
import hashlib as h




parser = optparse.OptionParser('usage %prog -F'+\
                               '<target file>')
parser.add_option('-F', dest='filename', type='string', help='specify target filename')
(options, args) = parser.parse_args()
fname = options.filename

md5 = h.md5()
sha1 = h.sha1()
sha256 = h.sha256()

with open(fname, 'rb') as f:
    for chunk in iter(lambda: f.read(4096), b""):
        md5.update(chunk)
        sha1.update(chunk)
        sha256.update(chunk)
print('MD5:  ',md5.hexdigest())
print('SHA1: ',sha1.hexdigest())
print('SHA256: ',sha256.hexdigest())
