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

