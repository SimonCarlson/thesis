7/3-19:
Restructured DTLS profile a bit

Spoke with Marco and Rikard. Large difficulties achieving true end-to-end encryption. How do you manage keys? How do you account for devices being deployed after an update is created but still needing that update? In Marco's and Ludwig's paper they introduce a dispatcher that can mediate between devices and users, allowing an update to be applied reactively instead of completely proactively (precondition timestamp is proactive). Having a local dispatcher (my case update server) receive a remote update then obtain a decryption key before encrypting it with a group context key works. Only encrypt0 in Contiki-ng (no sign0, encrypt1, or sign1). Can still be used for my purposes. If necessary can try to port sign0 from the Java impl. CBOR should be at least partially available in Contiki-ng as part of encrypt0.

Improved introduction with new sources on IoT security

Refined research question, made it narrower

Trying a new title, hopefully it sticks

No links to RFCs in bibliography

6/3-19:
Added OSCORE section in background

Made links in ToC

Separated conditions and directives in manifest format into pre/post conditions and pre/post directives. Updated image and text accordingly

Figures showing the protocols used in the DTLS and OSCORE profiles

Put architecture, life cycle, and profiles in a method chapter. Made the use of "chapter" and "section" consistent.

Should prepare some suggestions of titles and ask Shahid, maybe for research question as well?

Improved the introductions and summaries of chapters

Discussion about the protocol figures in the profile chapter

5/3-19:
Restructured chapter 5 into a DTLS and an OSCORE profile

Fixed acronyms in chapter 2

Prepared background section for OSCORE (very short)

Every chapter starting from background now ties together the previous and following chapters

First attempt at fixing problem statement

4/3-19:
Proper formatting of section 5.1 title

Clarified why UUID5 is used over UUID3

Improved formatting of SUIT architecture requirements list

Spoke to Shahid. Profile chapter should still be split up in two, in the second part refer to the mutual information from the first. Instantiate the procedure flow image with protocols or profiles so an implementor knows where to look for what. DTLS and its standards are much more mature than OSCORE and its standards. Tie together chapters with short summaries and introductions stating why this chapter. For application development, start with native. Flipping image - if time allows, not the highest priority. Differential updates are ambitious to pursue. Regarding COSE in Contiki: Martin Gunnarsson and Santiago (through Marco), there is a Java implementation.

Meeting with Farhad. Research question should be rephrased so that it is actually possible to answer it, current is too broad. Title is too broad (already aware). Problem statement should be shortened. Consider putting all my contributions in a single method chapter. Possibly mention related solutions, including any work done on SUIT. Fix citation style, be consistent, no need for links to documents. For discussion chapter, mention other aspects of IoT security. Make sure introduction is understandable for people without prior knowledge. Mention weak parts of SUIT (authorization?). 

1/3-19:
Added paragraph on sustainability

Sent a mail to Shahid asking for his thoughts on my profile chapter

Looking for resources that can help development. Found a CBOR library and a COSE library, the latter depending on the former. The COSE implementation uses either openssl or MbedTLS, I guess openssl is too large and that one of the two must be present on the device. Libcoap can be used to make a server if I don't use native Contiki code, maybe that is easier?

I just want to go and squat

Looking at the CoAP examples in Contiki, seems fine to make both server and device implementation in it. Only uncertain part is how to send large payloads, cannot seem to get block transfers to work

The chunks example seems like a good start for a resource handler for the server

Maybe I should start with manifest generator, then when I have an example manifest try to send it without COSE, then send with COSE, then move on to device update handler?

28/2-19:
I've felt motivated the past week or so but now it's dwindling again. Strange how motivation seems to come and go. Is motivation the lack of hardship?

Profile chapter feels done, I really don't know what else to put in it outside its current state

Want to move on to implementation. Do I start with Contiki development? Maybe I should just to understand how to use the DTLS/CoAP stack. Should lay out a plan for the prototype

Installed libcoap, managed to use DTLS via OpenSSL and PSK. Don't know if I can use that or if TinyDTLS is required, we'll see. Also, difference in using PSK and cert concerning my evaluation?

Managed to generate a X.509 cert with openssl and I think use it for a PKI-based coaps exchange in libcoap

Added paragraph about vendor and class ID generation, put it in a section with choice of hash algorithm

27/2-19:
Managed to define what I think the profile should cover (key algorithms for communication, hashing algorithms, encoding of payloads, encryption of payloads)

Added discussion on choice of ciphersuites and hashing algorithm

Mentioned EST-coaps and its compability

Mentioned ACE and its compability

Restructured the profile chapter as the DTLS/OSCORE profiles are much too intertwined to make sense as different section. Instead, sectioning on content of profile like in the RFCs

Almost got the hang of it but still not

Spoke to Marco. Out of scope for this profile to specify ciphersuites. Enough to use COSE signatures over DTLS/OSCORE, how would COSE encryption handle keys between all devices? COSE in CoAP (no OSCORE) is still not end-to-end. Group OSCORE enables multicast but does not secure channel like with DTLS.

26/2-19:
I'm not sure git branches are worth using in this project. Notes and the rendered thesis are a hassle to handle between branches and they don't really add anything since I have complete control over the repo anyway

Added acknowledgements placeholder

Separated RISE supevisor from KTH supervisor

Added keywords in Swedish as well

25/2-19:
The profiles will most likely be very small. SUIT does not require very many configurations to be chosen apart from protocols. Key/hash algorithms are the obvious ones.

Started writing a section about manifest format. 

I feel manifest format and profiles are the two things left before doing an implementation and evaluating it. Two more weeks for those parts leaves six weeks for implementation before a month of evaluation. Reasonable?

My initial spec of the manifest format seems sane. I have some arguments as of why I think it is a good format and it covers all elements mentioned in SUIT, so it ought to be good to go

Unsure about the difference between precursor and dependencies, and why do they mention encrypting the image requires a symmetric key? Is it too large for (feasible) asymmetric encryption?

Made a schematic image of the manifest format, still technology agnostic. No packet structure

21/2-19:
Thinking about profiles. Obvious inclusions are choices of protocols for communication, enrollment, and authorization. What else? Should I define message types and message exchanges? Endpoints? Format of registration requests and update polling? Key algorithms?

Found a quote in the SUIT architecture document leading me to believe they do in fact care about both firmware and application software (luckily)

Trying to figure out how to structure the manifest. Optional elements are optional to implement so thinking of doing them as options like in CoAP and have all mandatory elements in the manifest always, allowing the conditional ones have a zero-code.

Should the conclusions of the thesis contain security considerations naming threats identified in the suit model the architecture does not currently hinder?

Spoke to Shahid. Absolutely fine to break out optional elements and only keep mandatory as baseline manifest. Niclas Finne can probably help with how to parse dynamically sized packet elements. Profiles should provide the information needed to run the protocols suggested. "Close to OSCORE for all SUIT things", for parts where SUIT suggests key algorithms etc choose to be close to OSCORE/DTLS.

In CoAP there is a 128 bit elliptic curve hash.

20/2-19:
Spoke to Marco about citation, it is not needed.

Restructured the repo a bit and made READMEs for all directories

Removed ACE specifics from architecture part

Emphasized when new concepts are introduced

Revised actors, authorization, profiles, and upgrading

Wrote a preliminary draft on the life cycle

Found a CBOR library for constrained devices

Started pondering about profiles. What should be included?

"While the main goal for this document is to protect CoAP messages using DTLS 1.2, the information contained in the following sections is not limited to CoAP nor to DTLS itself." RFC 7925. Maybe this is an approach I should take for my thesis? My the main goal would then be to present a DTLS/CoAP based update architecture using EST-coaps for enrollment and constrained ACE tokens for authorization while having it be applicable for other protocols. Or maybe not since Shahid seems more interested in making some kind of superset of SUIT

19/2-19:
Alarm didn't go off for some reason. Working from home instead

I want to mention the four different tokens suggested by Marco. How do I cite that? It is not my idea originally.

Expanded on different key pairs

Added the different tokens

Explained the new use cases

18/2-19:
Brief meeting with Marco, he thought the thesis was well structured but had some issues utilizing the ACE framework properly. Traced back to my poor understanding of the framework, mailed Ludwig some questions. Other than that there were some minor flaws. One important point is: what does my architecture add on top of SUIT? It is still trying to be technology agnostic. I can see my architecture providing a way of adding certificates and tokens as well as profiles, but the working group might not be interested in profiles.

Marco mentioned my possible contributions to his and Ludwig's paper would be in the related work area concerning SUIT. It is not a huge, high flying paper but rather a look at existing propositions

Produced new figures showing more concrete but somewhat contrived examples

Included server authorization in update flow image

15/2-19:
Very constructive meeting with Shahid. Main takeaways: anything that is not in the SUIT standard goes into my architecture. Instantiate architecture in different use cases needing different functionality. Present the update procedure workflow image first, then dig deeper into each part of it. Emphasize new concepts. Someone wanting to implement it should easily know what they are required to do. Make life cycle to its own chapter, it can be short (2-3 pages). Make a profile chapter with at least one but preferrably two profiles (DTLS vs OSCORE?). Implementation to evaluate overhead of update, evaluation of other work has already been done, make assumptions about tokens, certs, protocols etc, measure radio cycles and packet loss.

Ludwig and Marco offered co-authorship for their critical infrastructure update paper. Verdict will have to depend on if they really think my thesis overlaps with their field.

Re-arranged the thesis and sketched a new outline for chapter 3, 4, and 5. 

Constructed some contrived use cases for the topology examples.

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

