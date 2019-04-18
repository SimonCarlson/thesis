# Generated ECC key for client

openssl ecparam -genkey -name secp256k1 -out client.pem

openssl req -new -sha256 -key client.pem -out client.csr (all blank except challenge password 'client')

openssl req -x509 -sha256 -days 365 -key client.pem -in client.csr -out client-cert.pem

openssl req -in client.csr -text -noout

### Server certificate

Same as client but change all occurences of 'client' to 'server'

# Example manifest

./manifest.py example-manifest.json -i memtest86+.elf -v test -c test -u update/image -m 1

# Flash nodes

In the project directory:

make TARGET=zoul BOARD=firefly PORT=/dev/ttyUSBX project-name.upload

make TARGET=zoul BOARD=firefly PORT=/dev/ttyUSBX login

Tentative link-local IPv6 address: fe80::212:4b00:9df:9096 (from hello-world.upload example, found once, don't know how)

Flashing one with the server and one with the client seems to work..??? They connect after a while. Manifest turns out ok except crap data at the end making the parsing wrong. Server announces itself as root. Using this, I won't be able to transfer files though. 

Blue one on the right, blank on the left. Start server first, then client. Hope it works