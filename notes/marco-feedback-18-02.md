General
As as suggestion, you can explicitly narrow the scope on SUIT and
SUIT-based mechanisms from the start and the title, and include an
additional chapter to compare SUIT with alternative approaches
considered as related work.

Chapter 1.1
The focus of SUIT is actually on updating FW only, not generic SW
(see WG charter).
~~On top of what you say, SUIT does not define any new security~~
~~mechanism either.~~

Chapter 1.1.2 and 1.1.3
~~This seems to suggest an incarnation/instance of the SUIT~~
~~architecture, i.e. with exact communication and security protocols.~~
~~This seems to be what is going to be brought on top of SUIT as~~
~~baseline.~~

Chapter 2.1
When you discuss congestion control, you can definely mention the
IETF work Cocoa
<https://tools.ietf.org/html/draft-ietf-core-cocoa-03>
You can also mention OSCORE as alternative to DTLS for the IoT stack
<https://tools.ietf.org/html/draft-ietf-core-object-security>

Chapter 2.1.2
~~"The TLS handshake procedure assumes all handshake messages are~~
~~delivered reliably which is rarely the case in IoT networks." is~~
~~true, but just because you usually use UDP. CoAP can actually run~~
~~also over TCP (see RFC 8323), and in that case it would be fine to~~
~~use TLS rather than DTLS.~~
You may mention RFC 7925 as a profile of TLS/DTLS for the IoT.
"The parties authenticate each other via public key encryption, ..."
is only one possible case. They can instead go for a pure pre-shared
key approach. Also, if they go for public key encryption, client
authentication is optional.
~~"... cookie exchange to prevent DoS attacks ..." would better say~~
~~"to complicate". See especially:~~
~~<http://soda.swedishict.se/6010/1/IJIS_paper.pdf>~~
~~<https://tools.ietf.org/html/draft-tiloca-tls-dos-handshake~~>
~~"Since the (D)TLS handshake assumes asymmetric cryptography, ..." ,~~
~~see above.~~

Chapter 2.1.3
When you discuss congestion control, you can definely mention the
IETF work Cocoa
<https://tools.ietf.org/html/draft-ietf-core-cocoa-03>
~~"poll the server for a new manifest" would better say "pull the~~
~~server for a new firmware/software update", as you have not~~
~~introduced the concept of (SUIT) manifest yet.~~

Chapter 2.2
~~SUIT is not devoted to any particular security solution either.~~
~~However, it sets high-level security requirements (as you say later~~
~~in Section 2.2.1).~~

Chapter 2.2.1
~~You say: "This thesis will propose a technology agnostic update~~
~~architecture and implement a prototype of it using a DTLS/CoAP~~
~~stack." What is the "agnostic architecture" going to add with~~
~~respect to the SUIT architecture?~~
If you focus on a prototype based on DTLS and CoAP (and I assume
COSE for end-to-end security between the FW Author and devices), it
seems you are in fact proposing this as a particular, non-agnostic,
incarnation of SUIT.
As you also notice, you would not be friendly to brodcast deliver,
e.g. between FW Server and Devices to update, as long as you
consider DTLS or other transport-layer security solutions.
In Figure 2.3, is "Operator" simply an alias for "Author"?

Chapter 3.4
~~About the usage of the ACE framework, you say: "As updates will be~~
~~sent from operators through servers to devices, the devices need to~~
~~know the originator of an update is authorized to issue the update."~~
~~That's definitely required to know, but well in advance through~~
~~early settings and later verifiable by checking the signature of the~~
~~FW image as coming from a trusted Author. It is that signature that~~
~~proves you origination, but the trustworthiness of those sources as~~
~~entitled to originate the content in the first place has to be~~
~~(securely) learned in advance.~~
~~I am not sure that's something that ACE as such can help you with,~~
~~as it is in fact about issuing an Access Token to prove one is~~
~~allowed to access a particular resource with a particular scope at a~~
~~particular host/audience.~~
~~I believe that ACE is still useful to use, although for different~~
~~reasons and in a different way:~~
~~1) On behalf of the owner of the FW Server, you need to provide FW~~
~~Authors with Access Tokens to upload FW images on the FW server.~~
~~2) On behalf of the owner of the FW Server, you need to provide~~
~~devices with Access Tokens to request FW images on the FW server~~
~~(PULL model), or to register and upload new settings/configurations~~
~~of their own on the FW server.~~
~~3) On behalf of the owner of the Device, you need to provide the FW~~
~~Server with an Access Token to provide that Device with FW images~~
~~(PUSH model).~~
~~4) On behalf of the owner of the Device, you need to provide the~~
~~Author with an Access Token to provide that Device with the FW~~
~~manifest, in case of split provisioning of FW manifest directly) and~~
~~FW image (through the FW Server).~~
Note that (2)(3)(4) can take advantage of the ACE signaling of its
profiles to indicate the security protocol that the FW server and
the Device have to use to communicate.

Chapter 3.5
With reference to the workflow and Figure 3.2:
1) I suppose "Operator" is the "Author" in SUIT, as the one building
the FW image. However, in SUIT it is the "Device Operator" that uses
the "Status Tracker" to check with the Device (not with the FW
server) if an update is necessary. See Section 5 of
draft-ietf-suit-architecture
2) Again on the usage of ACE, the described workflow has the Access
Token issued to the Operator. This would be just fine if the
Operator and the Device communicated directly, establishing a secure
channel as indicated by the profile claimed in the Access Token.
Here instead the Operator offloads the updating process to the
Update Server (FW Server), which is going to be the actual entity
accessing the Device for updating, but it is not the Token holder in
the described workflow. That is, an updating access as authorized by
the Access Token would be expected from the Operator. In fact, the
Access Token is bound to a Proof-of-possession key handled to the
Operator by the Authorization Server. Thus, the Device expects that
key to be used (e.g. to open a secure channel) by whomever tries to
do what is authorized by the Access Token, to prove it is indeed the
intended Token holder. Of course, the Update Server does not have
such a key and is not the Token holder.
See also the comments about Chapter 3.4 on the usage of the ACE
framework.

Chapter 3.7
See also the comments about Chapters 3.4 and 3.5 on the usage of the
ACE framework.