# Generated ECC key for client

openssl ecparam -genkey -name secp256k1 -out client.pem

openssl req -new -sha256 -key client.pem -out client.csr (all blank except challenge password 'client')

openssl req -x509 -sha256 -days 365 -key client.pem -in client.csr -out client-cert.pem

openssl req -in client.csr -text -noout

### Server certificate

Same as client but change all occurences of 'client' to 'server'

# Example manifest

./manifest.py 500-blocks-manifest.json -i 500-blocks-data.txt -v test -c test -u update/image -m 1

# Flash nodes

In the project directory:

make TARGET=zoul BOARD=firefly PORT=/dev/ttyUSBX project-name.upload

make TARGET=zoul BOARD=firefly PORT=/dev/ttyUSBX login

Tentative link-local IPv6 address: fe80::212:4b00:9df:9096 (from hello-world.upload example, found once, don't know how)

Flashing one with the server and one with the client seems to work..??? They connect after a while. Manifest turns out ok except crap data at the end making the parsing wrong. Server announces itself as root. Using this, I won't be able to transfer files though. 

Blue one on the right, blank on the left. Start server first, then client. Hope it works

# Generate random strings

import random

import string

random.seed(42)

"".join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(N))



# Energy consumption

*CPU energy:* cp = c*1.8/tm

*LPM energy:* lp = l*0.0545/tm

*Transmit energy:* lt = t*17.7/tm

*Listen energy:* lr = r*20/tm

*Total energy:* n = cp+lp+lt+lr

tm = c+l

where:
*tm* is the total time,
*c* is the time that the CPU was used.
*l* is the the time that the sensor was in Low Power Mode (LPM)
*t* is the transmit time  and
*r* is the Listen time

https://sourceforge.net/p/contiki/mailman/contiki-developers/?viewmonth=201701

# Connectivity

cd rpl-border-router

make TARGET=zoul BOARD=firefly PORT=/dev/ttyUSB1 border-router.upload

cd ../../tools/serial-os

sudo ./tunslip6 -B 115200 -s /dev/ttyUSB1 -t tun1 fd00::2/64

cd suitup

sudo ./update-server.native

cd hello-world

make TARGET=zoul BOARD=firefly PORT=/dev/ttyUSB0 hello-world.upload && make TARGET=zoul BOARD=firefly PORT=/dev/ttyUSB0 login

# Native connectivity

cd examples/rpl-border-router

./run-router.sh

sudo socat UDP6-RECVFROM:5683,fork UDP6-SENDTO:[fd00::302:304:506:708]

cd tools/serial-io

sudo ./tunslip6 -B 115200 -s /dev/ttyUSB1 -t tun1 aaaa::1/64

cd examples/suitup

sudo ./update-server.native

cd examples/hello-world

./run-hello.sh