14/2-19:
Added PDF graphics instead of tikz-figures
Added roles as a keystone, so there's now five of them
Added devices to roles, so there's now three of them
It makes sense to order the key areas keys->communication->authorization->updates because it follows the life cycle
Polished roles, key management, communication, authorization, updates, lifecycle
Renamed "updates" to "upgrading" (updating is the entire process, upgrading is the actual flip of images)
Rewrote most of the different architecture examples
Lots of boring work now such as fixing the fucking apostrophes..
After the boring work, give a proper read-through and mail to anyone interested. Prepare for criticism (should probably explicitly ask for criticism on upgrading chapter)
Should make an effort to standardize expressions - an update = manifest + image, upgrade = locally flip image etc
Restructured a bit and proofread chapter 1-3, merged branch with master, sent the thesis to Shahid, Farhad, Marco, Ludwig, Martin, and Joel. Hopefully I'll get some feedback
Right now it feels ok but I still don't feel I'm contributing with anything non-trivial

13/2-19:
Re-structured chapter 3. I feel this structure makes my thoughts come through in a more structured and convincing way. I can re use a lot of material I've already written and more easily expand some underdeveloped fields
i3 is pretty cool, starting to get the hang of it
Key management, first pass done
Authorization, first pass done
Communication, first pass done
Updating, first pass done
My updating discussion feels rather weak. I know too little about safe boot and bootloaders I feel
Should aim to make thesis look presentable and send to Farhad, Ludwig, Martin, Shahid asap
Maybe I should seriously cut down the amounts of Contiki-background. Do you really need to know anything besides it implementing standard protocols, having a process model, and events?
Life cycle, first pass done
Sketched all images that should be remade, won't be using tikz but instead draw.io. It just looks better imo

12/2-19:
Woke up 3:40 AM with a serious head ache. Sleep got completely fucked so worked from home today. Half day
Expanded the motivation for a life cycle and mentioned the four key areas. 
Added access control to the architecture but not yet done with that.

11/2-19:
Still feeling a lack of motivation, don't understand why
The architecture chapter should focus on the four key areas I identified: key management and distribution, authorization/access control, means of communication, and updating.
Are keys affected by updates? Maybe it depends on if devices are using a file system or not? If yes, keys are stored there so updating code should not affect it (permanent storage). If no, certificates and pre-shared secrets have to be distributed in code in order to re-enroll?
Studying models of authorization using ACE/OAuth2.0, hard to tell how abstract my approach should be. Right now it is purely schematic.
Authorizing the user seems enough. The servers are implicitly authorized through the updates they send (is it a security issue that they can send updates anyways?). Authorization server must be reached by devices and servers for introspection, yet again it may be proxied.

8/2-19:
Getting up within ten minutes of waking up seems to feel better
Meeting with Ludwig, Martin, Marco, and Shahid. Felt good. Overlap between my thesis and their research. They are interested in seeing what I propose. Will improve my thesis and send them my current work
Marco clarified differences between identity and authority: certificates proves the identity of machines and verifies who they are. Authority is about what they are allowed to do and will need some kind of access token (access control).
Expanded the server part, mentioning access control. Should write a separate section about it and embed in the architecture. Possibly put ACE in the background?
Meeting with Nexus and RISE members about PKI and security in IoT. Raised the question and need for access control, code signing, defining actors, interoperability between vendors.

7/2-19:
Improved the architecture image a little bit
I get all good ideas in the afternoon or at night, when I'm home or out walking. I don't at all feel as creative in the office
Improved the chapter about device life cycle and update architecture. Needs further discussion on roles.
Wrote about the proposed architecture, who can be considered a server and operator, and showed three example architectures.
Made placeholder images for these three examples

6/2-19:
Kept pondering about an architecture. SUIT presents one similar to what I have in mind, is this an issue?
Created a new chapter 3 dedicated to the architecture and lifecycle of devices. Transportation of images should be later, possibly last chapter before evaluation
My confidence has been declining as I feel less and less qualified for this task. At the same time I feel like I cannot contribute to anything. It is hard to stay motivated to work well
Wrote about the lifecycle of devices. Tried to include the perspective of enabling secure communications and profiles on server side. Drew a neato image.
Started writing about the actual architecture

5/2-19:
Spoke to Shahid. He offered insight on overarching purpose of thesis. I need to put more focus on the architecture of the mechanism, including the lifecycle of devices, how they interact with a server (profiles?), who can act as a server, and how keys can be generated and delivered to devices.
Mailed Ludwig Seitz and Martin Gunnarsson, they are researching secure IoT updates
Libcoap can be used for a mock server, pipe openssl signed payloads (manifests/images) to libcoap and send to a device
I have a much more abstract view of the architecture at large and lifespan of a device needing updates at some point. This is the topic for chapter 3.
Certificates are exchanged during (D)TLS handshake, and are not verified with a CA because they already contain the signature of the CA
A device needs to be shipped with their UUIDs, knowledge of how to register at a server, and at least one CA cert in order to verify certs of server and/or operator
Keep thinking, who is a server? Who can act as a server? Who installs/maintains/controls a server? In what cases can an operator bypass a server (manifest)? How does the server react if a operator bypasses it, does it care?


4/2-19:
Can generate very small and simple manifests from existing ones, reusing some attributes.
Made a GitHub repo for the manifest generator
Want to start looking at the parser, talk to Joel maybe? Should I make Shahid aware of what I'm doing or just keep going?

1/2-19:
Started on a manifest generator
Prepared for the ID2223 presentation

31/1-19:
Reduced the amount of detail in the CoAP chapter, put in a quote about upper bounds for message sizes.
Improved the style of listings and made them consistent.
Further improved consistency of text in the thesis
Started pondering JSON to CBOR manifest converter. CLI that either takes existing manifest and extracts format, vendor, class, and device. Can create new from scratch, specify parameters with flags. Must consider options so that interface does not become clunky (how much do I care about interface anyways?)
Put in list of tables, figures, listings, and abbreviations. Updated gitignore and build script accordingly
Split the image/manifest distribution image into two


30/1-19:
Improvements to Chapter 2. Better formatting, consistency, and style concerning section references and lists.
Made the presenation easier to understand without prior knowledge.


29/1-19:
Wrote some more on the presentation
Put all documents in the git repo, no point separating them
ARM mbed json-cbor converter and sbabic/swupdate can be used for inspiration but neither solution fits the thesis
Read chapter 8, 9, 11.2, 11.3, and 13 in the interconnecting book
Created a script that checks my .tex files for spelling errors. Fixed some spelling errors
Made a figure describing the modes of distributing images and manifests
Added todos about EST-coaps, interesting to speculate how it fits into the architecture

28/1-19:
"Epiphany". Mandatory elements in SUIT does not mean must always be present, it means it must be implemented to comply with SUIT. Can still put those fields in options to reduce manifest size.
SWUpdate: Made for Linux systems, only supports single image delivery, seems to assume there is a filesystem, assumes GRUB is bootloader, seems to use HTTP/HTTPS, seems to use symmetric encryption of images. Include in thesis as example of state of the art?
Using option delta and not just option codes can reduce size of that field for options with values exceeding X bytes but delta not exceeding X bytes.


25/1-19:
CoAP supports CBOR as content type. Option: Content-Format, Media Type: application/cbor, encoding: -, Id: 60
Sketching manifest formats
Trying to find a way to encode JSON in CBOR, maybe that is the way? Generate a manifest in JSON then serialize as CBOR
Did some more ID2223 work, should be done after today


24/1-19:
Rule of thumb: transmitting one byte is as expensive as running 8000 CPU cycles (Smart Objects With IP p. 374)
CoAP ETag option (entity-tag) tags different representations of resources so that they can be distinguished from each other
Sketched some SUIT manifest formats
Had to do some work for ID2223 as project submission is on the 27th
Wrote a really bad text about manifest format
Made the manifest format (3.1) text better but still have issues motivating my thoughts and don't know how to ensure I'm making the right decisions

23/1-19:
Cleaned up the thesis so far, made the introduction and background more coherent. Still unsure about the level of detail in the background

22/1-19:
Started sketching a header format for the manifest, created more questions
Structured the next chapter about the manifest
Found that Contiki-NG implements SHA-256, SHA-384, SHA-512, which can be used for the image digest
Spoke to Joel, he clarified it is Zolertia Firefly that is to be used. Wiki pages on Github
Gathered documents about Firefly and its components
Wrote a paragraph about Firefly in the thesis
Wrote up a few slides on SUIT. Not very substansial
Installed chromium with the Copper for Chrome extension to browse coap resources (https://github.com/mkovatsc/Copper4Cr)
Read the IoT in five days examples on Zoul and Contiki

21/1-19:
Both SUIT documents have been revised, the overarching information is the same with some added requirements and motivations to the information model
Restructured the SUIT information model part of the thesis
Read the paper on low-power CoAP with radio duty cycling in Contiki
My academic supervisor was changed to Farhad Abtahi
Started reading and writing on EST and EST-coaps
Structured the thesis source code by removing old comments, adding TODO comments, and adding skeleton subfiles for remaining chapters
The bytefield package in LaTeX can be used to draw network protocol stacks
Read about IPv6 and 6LoWPAN for my own understanding, probably won't include anything about it in the thesis

18/1-19:
Changed the order of the logbook so new entries are on top instead
Found a tool that helps me clean up the source code of the thesis
Improved the introduction, wrote introductory blurbs in the background chapter
Feeling positive about the work ahead of me, it feels more manageable after studying the details for a week. Will need at least one more week before doing anything concrete I estimate
Looked at CoAP examples in the Contiki-NG repo. Examples include both server-side and client-side code
Wrote about Contiki-NG. Processes, events, memory management, timers, network protocol

17/1-19:
Was introduced to Nexus by Shahid, told them briefly what I've been working on since Monday. Will schedule meeting with them some time (in one or two weeks?).
Kept writing about SUIT, mainly information model
Got an IoT book sent to me by Sam, co-written by a (former?) RISE employee

16/1-19:
Read about CoAP block transfer and the observe option
Read about EST-CoAP, might be relevant for when integrating the PKI
Found some documents about IEEE 802.15.4 and the usage of IPSec in 6LoWPAN
Wrote about the SUIT architecture, what requirements the draft defines, some terminology, and a proposed example architecture

15/1-19:
Installed Ubuntu over Manjaro
Set up Latex, Contiki-NG, and editor environments
Created a private Github repo for my thesis and structured it
Kept reading about CoAP, read about TLS and DTLS
Talked to Shahid, met Niclas Finne who is porting to Contiki-NG. He has studied flipping images locally a lot
Joel knows about what devices to use and can provide them
Was told about EST-CoAP, which is certificate enrollment over CoAP
The thesis should consider things like certificate enrollment, how to adapt SUIT to RISE's PKI system and light certificates, if the thesis can add to SUIT, if the thesis can add to Contiki-NG
Re-used some parts from the proposal to the introduction of the thesis

14/1-19:
Collecting documents about CoAP, CBOR, DTLS, SUIT, CORE
Reading about Contiki internals
Set up latex-template in overleaf
Installed Contiki toolchain natively

