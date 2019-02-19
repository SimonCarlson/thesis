# Parser

C-parser: define dynamic memory allocator as macro in header file, aim to have that as the only platform specific piece. Rest of implementation should work on any platform. Provide function to register an update handler which processes the parsed manifest.

# Considerations

Stronger architecture. Consider the lifecycle of a device from being rolled out of the factory to being installed and updated. Also consider the server side. Device management will be a consideration from an architectural view but not implementation.

How to enroll devices, both with keys and server connections? Don't assume a device has a cert already, it must obtain one. Details can be left to EST-coaps or similar.

Who can be a server? Who is allowed to distributed updates? How can that actor know how to communicate with devices?

Update "checker" or similar mechanism on device should have separate key pair with update server since it should only communicate updates with that specific actor. Other key pair for all other communications. Security implications of enrolling two key pairs from one factory certificate?

Certificates = identity but not authorization. Tokens for authorization, talk to Ludwig. Preferably, obtaining and validating tokens would be opaque like the PKI currently presented

# Key points

The architecture needs to account for: roles, key distribution and management, means of communication (profiles), access control, local updating and patching. These are the key ingredients

<b>Roles of operators, servers, and devices</b>: How to define servers, operators, and devices
<b>Key management for IoT update procedure:</b> pre-shared secrets, PKI w/ CA, certificates
<b>Device communication and profiles:</b> registering devices at server, updating profile after update, operators querying servers
<b>Update authorization:</b> ACE tokens. Somehow authorize parts of code? Authorize memory access? How to define roles?
<b>Update handling:</b> extract image and prepare bootloader, restart. Is it possible to hotswap code by changing memory addresses? Feels really wonky

# Prototypes

Maybe make two small prototypes, one DTLS and one OSCORE without using tokens to compare their efficency
~~Then make a "larger" proof-of-concept implementation using tokens~~
Prototypes should make assumptions about protocols, tokens, and certificates as they have already been evaluated. Instead try to get a working connection and measure radio duty cycles of the device and packet loss. Also, dummy update handler since upgrading images does not affect network traffic? Still energy consuming so is interesting.

# Key pairs

If the same key pair is used for different services, it becomes more valuable. Losing that key means higher risk.
Keys for device-to-device communication stay in the constrained network. Keys for update might leave the constrained network when servers and operators identify devices.
Might be too expensive to have several certificates per device. Also would that make enrollment more difficult, one PSK per key pair?