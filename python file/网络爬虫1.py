from urllib import request as r
import chardet as ch
ulr=input("Input the URL: ")
url_open=r.urlopen(ulr)
url_read=url_open.read()
Type=ch.detect(url_read)
print("The type is %s"%(Type["encoding"]))
