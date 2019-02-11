C-parser: define dynamic memory allocator as macro in header file, aim to have that as the only platform specific piece. Rest of implementation should work on any platform. Provide function to register an update handler which processes the parsed manifest.



Stronger architecture. Consider the lifecycle of a device from being rolled out of the factory to being installed and updated. Also consider the server side. Device management will be a consideration from an architectural view but not implementation.

How to enroll devices, both with keys and server connections? Don't assume a device has a cert already, it must obtain one. Details can be left to EST-coaps or similar.

Who can be a server? Who is allowed to distributed updates? How can that actor know how to communicate with devices?

Update "checker" or similar mechanism on device should have separate key pair with update server since it should only communicate updates with that specific actor. Other key pair for all other communications. Security implications of enrolling two key pairs from one factory certificate?



Certificates = identity but not authorization. Tokens for authorization, talk to Ludwig. Preferably, obtaining and validating tokens would be opaque like the PKI currently presented

The architecture needs to account for: key distribution and management, means of communication (profiles), access control, local updating and patching. These are the key ingredients

<b>Key distribution and management:</b> pre-shared secrets, PKI w/ CA, certificates
<b>Means of communication:</b> registering devices at server, updating profile after update, operators querying servers
<b>Access control:</b> ACE tokens. Somehow authorize parts of code? Authorize memory access? How to define roles?
<b>Local updating and patching:</b> extract image and prepare bootloader, restart. Is it possible to hotswap code by changing memory addresses? Feels really wonky