gae_xero
========

Playground for testing xero integration with google appenengine

Ive stored private information in the private subdirectory. The following commands should get the system working:
```
mkdir private
cd private 
openssl genrsa -out privatekey.pem 1024
openssl req -new -x509 -key privatekey.pem -out publickey.cer -days 1825
openssl pkcs12 -export -out public_privatekey.pfx -inkey privatekey.pem -in publickey.cer

touch __init__.py
echo "consumer_key='my_consumer_key'"> secret.py
echo "consumer_secret='my_secret_key'" >> secret.py


```

Links that may be useful:

https://github.com/freakboy3742/pyxero

http://developer.xero.com/documentation/advanced-docs/public-private-keypair/

http://stackoverflow.com/questions/21868826/access-xero-from-google-app-engine

http://hustoknow.blogspot.com.au/2012/01/using-pycrypto-instead-of-m2crypto-on.html


