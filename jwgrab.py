from bs4 import BeautifulSoup
import urllib2
import re,sys,getopt
val_array = "";
val_string = "";
val_size = -1;
ifile='';
ofile='';
myopts ="";
args="";
try:
    myopts, args = getopt.getopt(sys.argv[1:], "i:")
except getopt.GetoptError as e:
    print (str(e))
    print("Usage: %s -i input -o output" % sys.argv[0])
    sys.exit(2)

for o, a in myopts:
    if o == '-i':
        ifile = a






def js_to_py_re(rx):
    query, params = rx[1:].rsplit('/', 1)
    if 'g' in params:
        obj = re.findall
    else:
        obj = re.search
    # May need to make flags= smarter, but just an example...
    return lambda L: obj(query, L, flags=re.I if 'i' in params else 0)

import string

alphabet = string.digits + string.ascii_lowercase

def enc(n, base=36):
    out = []
    while n > 0:
        n, r = divmod(n, base)
        out.append(alphabet[r])
    return(''.join(reversed(out)))

url = ifile
print "Parsing the data"
soup = BeautifulSoup(urllib2.urlopen(url), "html.parser")
# print soup.prettify()
for line in str(soup).splitlines():
    if "eval(function(p,a,c,k,e,d)" in line:
        tmp_str = line.split(" p}(")[1]
        val_string = tmp_str.split(",36,125,")[0];
        val_string = val_string[1:-1]
        val_array = tmp_str.split(",36,125,")[1];
        val_array = val_array.replace(".split('|')))", "")[1:-1]
        val_array = val_array.split('|');
        val_size = len(val_array);
        print "Grabbing Videos"
        # print val_string

for c in range(124,0, -1):
    print "Searching the link"
    st = str(enc(c))
    s = 'r"\\b3g\\b"g';
    man = re.search(str(st) , str(val_string));
    # print
    # print val_array[c];
    if val_array[c]:
        val_string = re.sub(r"\b%s\b" % (st), val_array[c], val_string);


urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', val_string)
# print urls
for i in urls:
    if "v.mp4" in i:
        print "Found the link"
        print i

