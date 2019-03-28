# Generated ECC key for client

openssl ecparam -genkey -name secp256k1 -out client.pem

openssl req -new -sha256 -key client.pem -out client.csr (all blank except challenge password 'client')

openssl req -x509 -sha256 -days 365 -key client.pem -in client.csr -out client-cert.pem

openssl req -in client.csr -text -noout

### Server certificate

Same as client but change all occurences of 'client' to 'server'

# Example manifest

./manifest.py example-manifest.json -i memtest86+.elf -v test -c test -u update/image -m 1