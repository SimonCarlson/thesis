Chapter 3 of thesis: write what the goals of my design is (size) and motivate why to use the bare minimum. Present those elements, and tell which issues are covered by them. Present optional elements, motivate why they are included as options, tell their use cases are not critical but rather functional.



C-parser: define dynamic memory allocator as macro in header file, aim to have that as the only platform specific piece. Rest of implementation should work on any platform. Provide function to register an update handler which processes the parsed manifest.



Stronger architecture. Consider the lifecycle of a device from being rolled out of the factory to being installed and updated. Also consider the server side. Device management will be a consideration from an architectural view but not implementation.

How to enroll devices, both with keys and server connections? Don't assume a device has a cert already, it must obtain one. Details can be left to EST-coaps or similar.

Who can be a server? Who is allowed to distributed updates? How can that actor know how to communicate with devices?

Update "checker" or similar mechanism on device should have separate key pair with update server since it should only communicate updates with that specific actor. Other key pair for all other communications. Security implications of enrolling two key pairs from one factory certificate?