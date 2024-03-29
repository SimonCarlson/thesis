5/6-19:
Meeting with Sam and Joel to discuss the way forward for them.

Left the keycard, Firefly devices, dissertation, and sniffer at RISE.

Submitted my final draft and active participation signatures, and thanked Shahid and Farhad

I did it!

31/5-19:
Rolled back the repo to a better commit

Changed the README, added comments

30/5-19:
New graphs are in the thesis

Should send final thesis to Elena, she can ask them to delay the publishing until later

I think the thesis is done

29/5-19:
Made some graphs with error bars in matplotlib

Joel asked for the outline, sent it to him

28/5-19:
Sam's opposition went well

Meeting with Shahid, Joel, and Sam. Gonna help them carry on my work. Should prepare roll the repo back to a good point, make a README, and comment the code a bit

27/5-19:
:^)

24/5-19:
Finished Sam's opposition report and gave him a hard-copy of his report, annotated.

Generated a cover with a TRITA number, split it up, and included it in my own tex source. Easier than I expected.

Should speak to Shahid about way forward. Personally, I'm content with just finishing up whatever feedback I have left from Sam and submitting. He probably has more ideas though.

Spoke to Shahid. For the thesis everything seems fine. Just fix the feedback, prepare the code so that someone (Sam) can get into it. He seems very opimistic about writing a paper though. I'm yet to decide about it.

23/5-19:
Had my presentation. It went well.

Went through Sam's thesis. It's good, not much to complain about. Did not make a huge effort correcting the language since he is a native speaker and writes well. Gotta find some points, like 3, to bring up at the opposition. Thinking his choice of data structure (why not some other probabilistic data structure), conditions where compressed CRL outperform FCV, and something else..

22/5-19:
Gonna fix the rest of Sam's feedback after the presentation. Should print out his and get started with it after presentation as well.

Adding small cues so I won't get lost when presenting.

Practiced it again, 24 minutes now. Should I assume I have 25 minutes available and not 20? Should probably assume 20..

Practiced it again, 21 minutes. Felt better. Has to be good enough.

21/5-19:
Revising the presentation even further. Got down to 21 minutes sharp but still speaking quickly. Removed part about number of certificates as it doesn't feel central.

Addressed most of Sam's feedback in the report. Major parts left: decide what to do about EST-coaps and Contiki-NG in the background (thinking keep the first, drastically reduce the second). Standard deviations in results, should wait until after TSCH stuff has been (not) solved, after presentation. Consider more security implications (also after presentation and more feedback?)

20/5-19:
Got opposition report and feedback from Sam. Nice to have a native speaker correct the language. Some things are obvious must fix, such as proper delimitations of the work, removing some of the repeated content, and moving experimental setup into the implementation section. Others I'm not sure about. The work is based on SUIT as that is the entire premise of the thesis project (it has to start somewhere) and SUIT itself contains a lot of motivation around threats and issues concerning updates. I don't feel I would do a better job describing these things or that copying them into my thesis would add anything to it, hence explicitly mentioning these things are in SUIT.  I feel the security considerations mentioned are specific to my protocol/implementation, however I might find some more from SUIT. 

Way forward: completely prepare the presentation. Fill in the assessment template. Start working on Sam's feedback (although leave a copy of the thesis submitted for presentation). Start looking at TSCH and DTLS again.

Presentation is at ~21 minutes rehearsed but I'm talking very quickly. I wonder if it's even possible to cut more content at this point. Key management, profiles, and authorization are all really key. Roles are short already. Update handling, just mention it's not really covered but as long as you store parts of the manifest you're good? Going through the requirements of SUIT takes a lot of time but I have to present my results. I don't feel the life cycle is that important for the presentation.

Mailed Elena, she did not think of the assessment template as necessary. It is for grading, but nowadays thesis projects are P/F. It is sufficient to have examiners mail her of my participation as an active listener. Where do I find these projects? Not many are posted on Canvas. Should start looking.

Fixed the build script so ToC includes bibliography.

17/05-19:
I don't know if I can solve the TSCH and DTLS issue. I created a minimal example only sending one request and nothing else. The server gets stuck after "server hello verify was sent" and at the same time the client reports udp: bad checksum. Not using TSCH does not cause this, not using TSCH with DTLS does not cause this. Only TSCH and DTLS causes this. It does not seem to be related to the application, but is an issue in the OS itself. 

Asked for help in Gitter, hopefully someone picks it up. Saw they released a new version, 4.3, cloned it and tried my minimal example, no visible difference.

Running it with and without TSCH but always with DTLS: it looks basically identical up until the point the servers send a verify hello message and the client complains about bad checksum. Is it something in TSCH that causes the server hello verify to break? Fragmenting? I don't think that's a consideration for the MAC-layer. SICSLOWPAN_CONF_FRAG 1 still causes bad checksum. Dramatically increasing QUEUEBUF_CONF_NUM (3 to 16) still causes bad checksum. TSCH_CONF_MAX_INCOMING_PACKETS 16 (from 4) does not help. TSCH_SCHEDULE_CONF_MAX_SLOTFRAMES 16 (from 4) does not help. TSCH_PACKET_EACK_WITH_SRC_ADDR 1 (from 0) does not help. TSCH_CCA_ENABLED 1 (from 0) does not help. TSCH_RADIO_ON_DURING_TIMESLOT 1 (from 0) does not help.

Setting TSCH_CONF_MAX INCOMING_PACKETS 16, TSCH_SCHEDULE_CONF_MAX_SLOTFRAMES 16, TSCH_CCA_ENABLED 1, and TSCH_RADIO_ON_DURING_TIMESLOT 1 together does not help.

No progress today.

16/05-19:
TSCH and DTLS does not work. Best results so far is that they exchange keys and nothing more. It fits though, somehow, but without UIP fragmentation. I hope that isn't needed...

How should I structure the presentation? Maybe pick out the most important parts from each section? Many things will have to be omitted but that's fine. Consider what the most important parts that constitutes the thesis are and present just those?

Got the templates for assessment and opposition. Should probably have the assessment thing with me when I present, I don't really understand how it works but wanna be on the safe side.

DTLS and TSCH is apparently very tricky. Joel put me in touch with Nicolas who has managed to use both at the same time, I hope he can help (yet to answer).

Sent the current draft (old results) to Elena and Farhad. Also gave Elena information about the presentation so she can announce it.

Made it so the chunk sizes in the client and on the server works based on the project conf chunk size. Can send chunks of 32 or 64.

Turns out DTLS cannot handle chunk sizes of 64 without fragmentation, and I cannot fit all three of fragmentation, TSCH, and DTLS

Spoke to Niclas about TSCH and DTLS. He doesn't know much about it but gave some helpful suggestions. It seems, through TSCH logging, that the server just stops receiving and transferring messages at some point when using DTLS. Tried increasing incoming buffer size to no avail.

Response from Nicolas: TSCH latency can be adjusted through ORCHESTRA_CONF_UNICAST_PERIOD (should be prime). RAM can be doubled by disabling sleep mode 2 (DLPM?) through LPM_CONF_MAX_PM 1, limiting it to sleep mode 1 (LPM?). 

Debugging the DTLS and TSCH thing for nine hours today. No results. Tips from Niclas and Nicolas did not seem to help. Maybe I'm missing something. But no progress.

15/05-19:
Changed header in results tables

Included mention of operating system in abstract (code sizes)

Removed the conclusions header

Decreased font size in headers, better readability

Apparently Contiki-NG does not use time slotted channel hopping as a default. This means the receiver will be on a much larger portion of the time. Enabling it would cause the energy consumption by the radio in receive mode to be relative smaller and the transfer mode relatively larger. CPU times should be completely unaffected I believe. I cannot for the life of me manage to enable it. Despite changing memory allocator for the parser and eliminating about 1 K bytes in the stack region, TSCH and its service consumes so much memory. I am 688 bytes short, despite allocating roughly 500 in my client... I don't undestand

Maybe it's not too horrible if I present the setup properly, i.e. that I'm using the default MAC settings. Reasoning why is just that I didn't know, and didn't become aware of it until after the presentation was booked and I've gotten the draft approved and everything. It feels horrible

Still, the current results would have to be presented with it mind and with the note that relative receive energy use should go down and transfer energy use go up. It weakens the point of delving into differential updates from an energy consumption view but that's still valid because of use cases, stronger authentication model, and overhead.

Have to speak to Shahid. Until I can catch him, finish whatever else with the report.

Spoke to Shahid. For the presentation it is ok but still less good. I will have time after to fix it, meaning it really has to be fixed...

Will get feedback from Elena. Priority is to fix that and give Sam draft tomorrow. Prepare presentation. Try to fix the code asap. Finish the thesis.

Feedback from Elena was very positive. She had just a few corrections about tense mainly. She complimented me on my writing. Felt nice.

I have TSCH working in my application and server. Unbelievable. I'm actually getting DLPM measurements now, mA for that? Power mode 3? Introduced CoAP bug where the first register message is not responded to, inflates (CPU) energest register numbers for client.

In order to fit TSCH UIP fragmenting had to be turned off. This in turn means sending vendor id, class id, and version as a URI query does not work (breaks without fragmentation). I did not figure out how to receive block-wise messages at the server. Thus, the server just recieves the first parts of the attributes and writes very little to a profile. The profile was just for concept anyways and is not used, hence I opted to just continue with the evaluation.

14/05-19:
Farhad mailed me his feedback. It was surprisingly few and small comments, however I don't know what I base that judgement on (being pessimistic?) Will fix quickly

I realized I had put the use case requirements in the information model evaluation. Changed it to security requirements, motivated them in the same way. Should probably go through one more time at least

Implemented changes based on Farhad's feedback. Smaller font size in tables did look really nice actually

Fixed most (all) floats, unsure about the last table taking up an entire page... Something will, but maybe it looks odd

Mailed Elena the draft, asked about May 23rd, she confirmed 9:00 would work, just waiting for Shahid now. Should inform Sam (tomorrow perhaps) and give him the draft

13/05-19:
As soon as dates for presentation gets mentioned I get so stressed. Having to wait for someones approval to book a date with another person with constraints on four people being there is so difficult to handle. Why can't I just pick a date?

Starting work on presentation slides.

Should I even prepare notes for the slides? I want to talk freely and I know enough about my own work (hyuk hyuk) to do so but it is rather long and having notes might help me pace better. Either way I should prepare notes for difficult questions I anticipate

Banking on being able to mail Elena tomorrow about dates after meeting with Farhad.

Got dates from Sam that works for both Elena and Shahid, it's rather soon... Doable but soon

Presentation should be pretty easy to prepare for, I just have to pick out the most relevant parts. Good advice that presentation and report are two different things

10/5-19:
I don't know what to do with code size. Still so difficult to ensure I sum all correct parts. I obviously include my own code, and should include COSE. But where do I draw the line? I don't think I should include anything CoAP related. What about standard library imports? Don't know if some of them already are/would be imported. 

Saw in Canvas there are submissions for alpha/beta draft, I have not submitted anything... Mailed Farhad about it

The assessment template is rather long. I guess you only fill one in for yourself?

According to Sam the energest measurements seem way off for certain measurements. CoAP request measurements seem trustworthy but stuff like encryption/decryption seem much too low. Would explain the low results I found when decoding and parsing. What to do?

Energest issues might be related to the scale of operations being measured. Looking at my own results it seems like all messages and callbacks could be/are accurate and just the (entirely local) manifest decode and parsing is way too low. Maybe explain that in the thesis and don't include those measurements? Is that honest?

Started thinking more about security considerations. How contrived can an example be? Obviously you can do a lot of implementation errors that causes issues but that feels irrelevant. What are the considerations on a high level?

Added parts about content key distribution methods for COSE signing.

I measured the decryption and parsing code. For one pass in the application (the measurements of the thesis) it would consistently yield 110-111 cycles (0.003 sec) which seems suspiciously low. Running the code 100000 times the measured wall time was 5m 32s which is 332 seconds. RTIMER_NOW() reported a diff of 10876410 ticks which is 331,9 seconds, and energest reported 10876095 ticks which is 331,9 seconds. 331,9/100000 ~= 0.003, which is in line with the previous results. It is also consistent with wall time meaning the timer itself seems reliable, even on smaller scales. Maybe I just keep the results anyways?

Acknowledgements can be added later according to Farhad.

9/5-19:
Had a discussion with Sam about energy estimations. We reached some numbers we both agreed to use in order to be consistent. Good to have it cleared up since he has an EE background and knows more about this stuff than I do

Updated the graphs and numbers relating to energy consumption estimation in the thesis

Divided the abstracts into paragraphs. Maybe they are quite long? Possibly the motivation can be shortened a bit, I think the point comes across anyways

Should probably look into the code size measurements but I don't think it's that clear cut showing sizes of "modules", but rather entities in code that are implicitly connected to modules. I know approximately how large my application code is so maybe I can add the relevant sections up and get the same amount of bytes? Would help contextualizing it by comparing it to other modules in the operating system

Added Energest citation, if anyone is wondering about the accuracy of the module they can go there

Fixed formatting issues. Should I try to reformat the tables, perhaps restructure the split between columns?

Exploring the ramprof and flashprof make targets to understand the sizes. Difficult to report on it correctly, how do I know I include everything included to my application and not other stuff? Also, do I account for all imports and COSE code? Thinking yes.

Should ask about the license in the source files. Also, decide about energest code (macros?).

8/5-19:
Fixed tokens, updated all text related to it and the high-level architecture image.

Time to check tenses? Time-consuming stuff but should probably do before sending to Farhad. Don't know if anything else is more urgent at this point. Maybe layout of figure, tables etc

Check tense, went through the entire report. Should be pretty good but I might have missed things, so prepare for feedback. Layout isn't entirely finished, two floats I'm unsure about how to place. It'll pan out though as the thesis will change based on feedback

7/5-19:
Remade the descriptive lists in the qualitative evaluation to tables (long tables)

Good progress on conclusions. Maybe leave it here until Shahid/Farhad comments further on it.

Added summary section to implementation

Meeting with Shahid. He's giving some good feedback mainly on figures to make the thing more understandable. And it even looks like a report! In general: make figures really clear and explicit even from just the caption (use full sentences as in the use case examples). Be clear when referencing/building upon SUIT. Mention COSE in the background (maybe alongside OSCORE?). Examine the size reporting tools of Contiki-NG to make the code size results more contextualized (maybe better than the bare-bones example?).

Wrote Swedish and English abstracts

Added some numbers related to the energy consumption of radio receive during image transfer (up to 67% and 64% client and server respectively)

Various fixes per Shahid's feedback

I must decide where to draw the line on certain topics. Some things can be discussed to no end but with diminishing returns of how much it actually contributes to the thesis. The way forward is to get literally every single section of the thesis in an acceptable state, then fix the things receiving the most criticism, then fixing the various things I feel like. Probably won't have time for the third part though but that's fine.

How personal do I get in acknowledgements? Also, is it weird to write them beforehand since I'll be thanking my examiner (before she's passed me?). Do I write them after my defense?

I'll very most likely abandon actual upgrades entirely as 1) it requires a lot of preparation with the image which in turn 2) requires a lot of work with the build system 3) it requires a alot of work with the bootloader, of which none I've done so far. It's too much work and I honestly feel it should be a separate thesis entirely

6/5-19:
Working more on my results. Cannot for the life of me get the sniffer working. Communication overhead results feel weak. At the same time, would checking packet sizes and latency really evaluate my solution and not DTLS in Contiki-NG? Not so sure about that.

Spoke to Farhad, this Wednesday I'll send him an almost complete draft and hopefully get some feedback and book a timeslot for presentation. Need to finish the results, conclusion, and abstract.

3/5-19:
Made the implementation description of client and server easier to follow

Added energy consumption and code size measurements

Started the discussion section

2/5-19:
Better day today. DTLS works when running client and server on boards.

Spoke to Rikard, he can procure a sniffer by tomorrow afternoon. Hopefully it works to get some data to wireshark.

Started measuring energy consumption of my prototypes. Measuring for 500, 2000, and 4000 blocks. Still not sure how to present it. Anything will work probably. Unsure about amps, but cc2538 datasheet should have it. Deep low power mode does not seem to be used.

1/5-19:
Forwarding via socat seems to break DTLS...

30/4-19:
Can connect client on board with native server through UDP forwarding using socat.

Cleaned up the code a little, made the register resource create a profile file and the manifest resource to read it.

DTLS probably won't work with UDP forwarding as the client tries to connect to the fd00::1 peer and not fd00::302:304:506:708. The hello requests and verify as routed properly but since theyre going to/coming from the wrong peer it doesn't matter... Back to square one. Ask Rikard about the sniffer? Maybe it's not too hard to use..

29/4-19:
Rewrote larger parts of the qualitative evaluation. Tried to be more explanatory and provide more angles.

Mailed Farhad the current state of the thesis (with preliminary qualitative results) and asked about when he thinks it is ready for booking a time slot for defense.

Started thinking about future work and security considerations.

Should ask someone about how to measure communication overhead. I know the 8/32 bytes of COSE overhead but not with DTLS. Really, really, really, really hope not running the server natively will interfere. How do I even sniff packets over the air with this setup? If I need another board USB ports will be an issue.. Adapters?

Energy consumption should be easier to solve, just gotta figure out the amps. Code size easy peasy.

26/4-19:
No further progress with connectivity. Starting tunslip as a tap interface only broke connectivity. CoAP messages to port 60001 does not work. Don't think I can bridge tun interfaces at all and don't know how to make native Contiki start as a tap instead.

Generating data from image resource, can change arbitrarily. Difficult to buffer into a coffee file on client, causes segfault AFTER everything (literally everything) is done (right before PROCESS_END). Checksum works.

What is the point of actually storing the file in this experiment? I'm just looking at transmissions anyways. Correctness? However, does it make transport more correct? It's a symptom of me not researching methods related to embedded file systems and flash storage. It doesn't feel like it hurts the thesis.

25/4-19:
No further progress with connectivity. Wrote two stack overflow questions and mailed Martin about it. Seems the IP packets do reach the server from the client (ping) but not CoAP. Maybe some forwarding issue? Enabling ipv6 forwarding and new rules in ip6tables did nothing (actually broke ping connectivity).

Some black magic stuff going on with the SHA256 update function, can seemingly update several thousands of KB worth of data before finalizing. Useful.

Thinking of implementing the file system interaction over buffer and then calling it for the implementation. Routing issues is more about experimental setup and I can use the two boards only in worst case. Should finish implementation and probably implementation chapter, and as much as possible in results (qualitative stuff). Also make placeholder for discussion section? Where?

Mailed zolertia support about electrical current values, am so uninitiated in the field that I don't even know proper terminology.

Storing the image data in a file instead of buffer. Should somehow test my mechanism when sending larger amounts of data. Might be tricky to hard-code very large strings....

24/4-19:
The 'image' file is now encrypted and decrypted blockwise.

The SHA256 ctx is updated blockwise, calculation works fine, but comparison is tricky because the hex representation of the ctx checksum equals the string representation of the manifest.

Some signs of connectivity between native server and embedded client. Start border router and tunslip on a different interface (-t flag) than the native process, start native server (which will be tun0), start client and you can ping the server from client but CoAP does not work.

23/4-19:
Voltage will be constant when firefly is in use. How do I know the current? It will vary. Does a certain mode have a specific current, like x mA for low power mode and y mA for transmission?

Spoke to Shahid. Gathered that locally upgrading an image would be very helpful for the thesis and might not be too complicated (speak to Niclas), but it would not be essential. Implementing and evaluating the communication would be enough.

The bug preventing the registration message from being sent was due to disabling the sicslowpan fragmentation. Enabling it solved the issue but requires a significant amount of memory. Could lower other configurations to balance it out.

Looking at encrypting and decrypting transfers block by block. Almost there, difficult since COSE adds 8 bits tag the content itself is only 24 bit, but the offset considers it 32 bits.

22/4-19:
My thesis and SUIT tries to achieve similar but not equal things. I see SUIT as a pair of high-level requirement documents for someone wanting to design an architecture. I see my work as an architecture backed by high-level requirements. Someone implementing my architecture in a real deployment would still have to create their own requirements with their deployment in mind, but these requirements would/could be of another nature such as more functional and measurable requirements. Furthermore SUIT does not have any ambitions of defining profiles or implementations etc, whereas my work does. My thesis is (just) one step down the abstraction ladder.

Is it the COSE code annihilating my stack? Trying to encrypt something in a simple for loop destroys the index variable when on the native platform.

Looked at the energest and Coffee filesystem modules. Feel better equipped to make some sort of evaluation. Still need to speak to Shahid about way forward.

19/4-19:
Running the server and a router on a board each: server and router can reach each other. When opening the tunslip6 interface, host can reach router, but not server. Does not work if server announces itself as DAG root.

If I get native server + border router + embedded client working, maybe I can try blockwise COSE encryption and store the file on the client using Coffee?

Is it interesting to compare energy consumption when encrypting an entire file at once or blockwise? Wouldn't that be evaluating the COSE implementation? Perhaps might still be useful.

Is it the ELF or bin file that's flashed onto the board?

Wrote a list on what needs fixing. Need help from people, probably Shahid and Rikard.

18/4-19:
Can have client and server communicate on boards without router. Does not solve problem with sending files as server does not have a filesystem.

Some weird bugs are present on the client, seems to stem from comparing character pointers to literals. Did some ugly fixes. The client can parse the manifest correctly and run the COSE and SHA256 functions.

How do I approach sending an image? I don't understand how the border router should work.

Really high stress levels today. Can't find any solace.

17/4-19:
Spoke to Marco about hardware setup, will need a second board to act as border router due to differences in physical protocol

Shahid gave me two boards to experiment with. One for a router, one for a client. Trying to understand the flashing process and ran into problems with code size exceeding the RAM for the client (server should run natively). Changed the project configuration in order to reduce the size (various network parameters were lowered). Unsure how a buffer for a large file will work out.. Maybe it won't

16/4-19:
Something wrong in the COSE encryption, only first 71 bytes are encrypted. Ciphertext length gets at some point truncated to a uint8_t but I've yet to find a fix. Mailed Martin.

The issue was using uint8_t for holding the length of the ciphertext. Changing uint8_t m_len to uint16_t where needed solved the issue.

Decoding and decrypting image file

Really hard to continue since I won't be able to send an actual file (Cooja).... Also how will I properly test my functionality? Hopefully there's some terminal I can connect to on the board whenever I can find one. Should speak to Shahid about it.

Successfully calculated the hash of image buffer. Hopefully it will not be length restricted.

15/4-19:
:^)

12/4-19:
Stateful transfer of a file from server resource. Now to do it with a really large file... Client memory allocation is still a hurdle

COSE encryption in image resource. Seems like not the entire data is encrypted, asked Martin about it. Maybe there is a limit and I should encrypt each block?

Example of SHA256 digest thanks to a kind stranger in Gitter.

11/4-19:
Added Contiki-NG and manifest-generator repositories as an appendix

Spoke with Joel and Niclas. They are looking into DTLS and certificates for Contiki-NG. Should I think of any requirements (non-functional) or configuration methods or the like I should tell them.

Big progress with COSE. Can send an encrypted COSE payload and decrypt it at the client. Would consider COSE done with the exception of sending an image (because I don't know how to send the image).

10/4-19:
COSE decryption fails at validating the tag. Don't know how to solve, mailed Martin

Sketching some questions for Joel and Niclas tomorrow. Hopefully they can also help with SHA256 in Contiki-NG and how MEMB works

Mailed Elena and asked about booking time for presentation

Getting a result from decoding and decrypting COSE but it does not match original plaintext.

Since the manifest structure of the thesis is just following the recommendations of SUIT it should already fulfill the security requirements posted upon it. More interesting is looking at the use cases I think.

Trying to encrypt COSE data in my manifest resource, if I memcpy from the cipher to some buffer it does not segfault, even if I don't use that buffer afterwards...

9/4-19:
Made a GitHub Gist and sent to Martin, hopefully he can help with COSE.

Got guidance on the COSE code from Martin, have a better understanding on how to use it. I think I've successfully encrypted a small message. Next step is to decrypt, and send it. Consider how to manage keys... Marco probably has an idea.

"Encrypt has a MAC so that's some kind of authentication" - Martin

Did a small preliminary qualitative evaluation of the architecture complying with SUIT. Should think of if it adds anything SUIT does not mention. Added it as a list in chapter 4

Some progress with COSE, decryption still difficult

8/4-19:
Mailed Joel about certificates and DTLS, apparently Contiki-NG does not yet support it. I wonder how it will work considering I'm working on an older fork of the OS... Maybe I can just extract my files since I (probably will be/) am using standalone files from Martin. Meeting proposed this Thursday.

I must continue elsewhere. Martin has yet to contact me back about COSE. I can look at the callback for the image handler, it must allocate memory for and reassemble a large file. Statically allocating space for a file that large feels so wasteful, it could easily be more than half of the flash for a Firefly board...

Really not sure how I am supposed to proceed. I don't understand the COSE code and Martin does not respond. DTLS won't happen until at least Thursday this week. Transferring a binary file won't work in Cooja as fopen() causes segfaults, and I have no hardware to run the client on with server on my computer. Do I try to qualitatively evaluate my architecture Tuesday and Wednesday maybe?

5/4-19:
Further described the manifest fomat, showed mappings of element names to integers, included (and formatted) an example manifest in JSON format. 

Improved the README in the manifest-generator repo, citing it in thesis

4/4-19:
Attempting to use Martin's COSE code. No success, immediate segfault when encoding data to CBOR. No idea how the code is supposed to be used, mailed Martin. Feels like this can take a very long time to fix...

Put implementation in methods chapter. Wrote shortly about the design of the prototype (including a sequence diagram of the server and client), and the manifest generator.

Created placeholder for evaluation chapter.

Added mention of developing server in Contiki-NG as proof of concept of capable IoT devices acting as update servers.

3/4-19:
Parser runs in Contiki and Cooja using only MEMB and its related functions to allocate memory. I'm wasting a bit of memory partially because I don't fully understand MEMB allocation, it did not work as expected. It's fine for now, better to spend time getting COSE and certificates to work.

Issues when building the OSCORE (COSE) code, cannot find references to security libs that are standard in Contiki. Also haven't been able to run just the COSE code, difficult dependencies. Gotta mail Martin.

2/4-19:
Still struggling with some stack-related issues. I don't know but I think I'm somehow ruining the stack so that removing arbitrary statements (thus changing the layout of the stack) causes segfaults. The code feels very brittle but I really don't know how to troubleshoot it.

Apart from still using malloc and not MEMB, the parser is running in the update client. I probably should try to fix that before looking at certificates and COSE. Maybe I should mail Joel meanwhile incase he is not available soon.

1/4-19:
Decided to opt for a functional "parser" instead of a good one, meaning I'm just handling the use case of one specific manifest (example-manifest.json). It is however easy to generalise it, you only need to loop the fields that are nested and that's it. I would rather have a working one for the purpose of an evaluation than a nice looking one with no time left to evaluate.

Maybe it is feasible to compare CoAP + DTLS vs OSCORE considering Martin's implementation? Would be interesting. Unsure if it is fair however since OSCORE will most likely not use certificates but rather PSK. Maybe I can do a certificate-based CoAP + DTLS evaluation then compare CoAP + DTLS with PSK to OSCORE.

29/3-19:
Been working on the "parser" all day. Not much success. Traversing the nested structures is really tricky and building linked structures of the data is harder than it seems. I've issues with the stack being corrupted, don't know how to debug.

28/3-19:
Rewrote parts of the manifest generator to reduce size of keys in manifest (also generated new example)

Spoke to Shahid, he got a call from Combitech. Writing a paper in August is feasible but could be tight on time (also few people are there).

Started a manifest parser. Its more of a naive pattern matcher because I'm not actually parsing and lexing etc, too heavy and time consuming. Idea is to extract keys from the manifest string, depending on the key extract value and fit into a manifest modeleled from structs. Final result will be a struct with smaller (nested) structs analogous to the format image in the thesis. Trying to avoid memory allocations at all if possible, doing some ugly stuff just to get it working.

27/3-19:
Listening to the IETF SUIT meeting. Nothing new so far, some liaison mentioned status trackers. My architecture contains a kind of status tracker implied in server logic, won't take action. 

They keys in the manifest should be mapped to integer values to reduce size. Why encode the value "1" with the key "version", waste of space.

Server endpoints must be static!!! That's the reason for my previous bug where the address of an endpoint would change. Also why block transfers did not work, the second block request would go to an invalid address and time out.

With Niclas' fix in coap-uip.c (adding case DTLS_PSK_HINT:) in get_psk_info function DTLS works with PSK. Now, how to make it work with certificates?

26/3-19:
Listening to live IETF summit about COSE. I am not familiar enough with the standard to understand the discussion as it is too technical, but it is interesting to see how the IETF operates and what they discuss.

The branch containing COSE/OSCORE code is older than the others and there has been changes in the network stack of Contiki since. Initiating the RPL DAG root is using a different function. Might be other inconsistencies, should probably stick to the COSE/OSCORE branch and explain in the report it is of a slightly older Contiki version.

Mailed Martin, he showed another repo with COSE/CBOR standalone files. Maybe I can just use those instead with the newer Contiki?

Spoke to Niclas. Native processes are the way they are, but there is a way to remove the Contiki network stack from the OS itself and run it using POSIX API. Joel knows more about DTLS and certificates in Contiki. According to Niclas callbacks for block transfers are fine, can't figure out the issue.

25/3-19:
Meeting Niclas tomorrow, hopefully he can help with native processes and DTLS

Trying to understand the block option of CoAP. It seems rather simple, your callback handler receives a buffer, offset, and preferred block size and it's up to the handler to copy data into the buffer accordingly. I assume for the prototype it is fine to open the manifest file and copy blockwise into the buffer. However, the handler function is repeatedly called upon, how to manage state of file? Static offset of file pointer? Same offset as for the message buffer?

Stacked view in i3 (super+s) is really neat when you want a window to be accessible yet not occupy space all the time

Cannot open files in filesystem while simulating in Cooja. For now the manifest is encoded as a string in the source code.

When using COSE, will the entire object be loaded and signed/encrypted and then buffered through CoAP blocks? Declare it as static, if null load and sign the payload, if not null send it block by block, when done set it null again.

22/3-19:
Still don't understand how native processes are supposed to work. I can find no indication of IPv6 address configuration or anything of the sort, only configurations for IPv4 that have no effect

Do I really need parsing in my implementation? It would be nice to just skip it since it has no actual effect on transport and security of updates, just simulating an actual update flow. However, if I measure code size the presence/absence of a parser must be taken into account

Feels difficult to finish in time, especially if I can't find any concrete help. Getting tips like "dig around in the IP stack" doesn't help when I don't know what I'm doing at all

The behaviour of the server will be the same no matter if I run it in Cooja or not except for maybe DTLS configurations. The resources should act the same no matter what. I can spend productive time implementing their behaviour and understanding how to sign/encrypt payloads in COSE.

Spoke to Shahid. Consider which elements of the update architecture, especially client side, would be needed to carry out further work. Parser should, for this reason, be included (at least a rudimentary one). Pre-generate and hardcode certificates but make sure to use correct ciphersuites (does OpenSSL support ECC? RSA won't cut it). Mailed Joel about availability of Firefly devices, Niclas about assistance with Contiki native processes and DTLS. 

For the moment, continue implementing client and server behaviours in Cooja and then migrate to actual hardware when possible or native processes when connectivity is solved.

21/3-19:
project-conf.h configs for CoAP chunk size and header size seem to have no effect on including the entire vendor and class ID strings, I think they still are too long. Block option?

By initiating the update server as a RPL DAG root connectivity seems to work without using my ugly hack in the coap driver

make with MAKE_WITH_DTLS=1 MAKE_COAP_DTLS_KEYSTORE=MAKE_COAP_DTLS_KEYSTORE_SIMPLE and define PSK user and key in project-conf.h for DTLS. DTLS connectivity does not work still though, cannot find peer (whatever that is and for whatever reason)

Shahid thinks native processes is a better idea because Cooja motes are old and for some reason asymmetric crypto will be harder to achieve. Using a PSK is probably symmetric crypto, no? Anyways native processes still don't work, must ask Joel.. My guess is still that the client can't send since it binds to the same IP of the server

20/3-19:
The RESOURCE macro accepts four handlers, one for each request type. 

When POSTing queries, it seems the message becomes malformed when exceeding 62 bytes. I suspect block transfer is needed since the vendor and class IDs are relatively large. When using short dummy values it works fine

The workflow of registering, GETing a manifest, and GETing an image works but is just a simple skeleton. Not sending the manifest, no DTLS, no parsing of manifest etc

18/3-19:
Rewrote my manifest generator to accommodate the new manifest structure

How will my Contiki server implementation read the manifest from disk? I presume that will require either a standard library or using the Coffee filesystem. Maybe I just use the standard library and don't care

Let the client GET manifest from well-known URL (such as update/manifest), implement server logic to determine which manifest it should receive based on its profile. The manifest contains URL for that specific update image (such as update/uniqueStringBasedOnSomething)

Implement and experiment in Cooja, port to Firefly, evaluate on Firefly?

If I don't run Cooja in the Contiki container I get tons of run-time errors during simulation but it compiles and launches well..

15/3-19:
Grapes

If a Contiki application run natively is opening a tun interface, can it still communicate over other interfaces? I guess yes.

In contiki-ng/os/net/app-layer/coap/coap-uip.c, changing the function coap_endpoint_is_connected to return 1 despite not having a RPL graph makes server and client communicate over CoAP. Obviously really shoddy method but it seems to work. I can now send messages in Cooja between two nodes.

14/3-19:
Still trying to communicate between two native Contiki clients. Cooja simulations do not work either but it feels much more difficult to debug/test

Launching the Contiki container with --net=host allows the container to use the same network stack as the host, meaning the container and host can send each other messages (tested with netcat)

Got Sam's libcoap server but I still think a Contiki server is the way to go because of COSE objects

Tried editing the global IPv6 address prefix in arch/platform/native/platform.c to no avail, cannot figure out how to change address itself

Cooja is still not finding connectivity. Do I have to add routers and stuff too? Maybe just the motes aren't enough

The implementation barring COSE seems so straight forward, if I make these problems work it should be much easier to proceed. I'm initiallity not doing any particular update handling, just communication

13/3-19:
It seems I am unable to run two concurrent native Contiki processes as they try to bind the same ip-address. Running the server and using the libcoap client works and wireshark can sniff the traffic, and just using the Contiki client but no server works in the sense that messages are sent and wireshark can sniff them. Starting the server and then the Contiki client yields nothing, the client cannot transmit.

Should I use Cooja instead? Maybe it is easier but using pure native processes feels like development iteration is faster. Optimal would be to have them use different IPs as expected but don't know how to do so.

Does using the blocking CoAP interface differ from using the callback one? I would guess no for my purposes since I'm not building an actual application. I could just use the blocking API to simulate a sequential process. Register -> get manifest -> verify -> get image. Sequential and easy.

12/3-19:
Started looking at how to implement a prototype in Contiki-NG

11/3-19:
I am exhausted

Where do we go from here? Implementation? Refining the thesis further? The layout for sure needs work but I feel the content is there. Perhaps introduction sections on COSE but does it really provide anything? Also, does the UDP section provide anything? Doubt it

What would the implementation start with? Creating a mock server and client exchanging COSE signed payloads over CoAP and DTLS perhaps. Then signing/encrypting payloads in COSE. Then move on to defining manifest packet structure, then implementing a small parser. Last piece is probably to do the actual update.

Improved the layout of figures. They now align better with their describing text and tries not to make the thesis look awkward. Removed the UDP header figure.

It's funny how the more you look at your thesis the less you like it, and looking at other people's thesis for the first time makes them look super.

8/3-19:
Maybe I should use vim after all

Added some discussion on achieving end-to-end encryption and key management

Suppressed repetitions of tables in list of tables

Forked Martin's contiki-ng repo containing cbor/cose/oscore code

Tried to understand COSE sign objects. Maybe I do a little

Sent the state of the thesis to Elena, Farhad, and Shahid and wished them all a nice weekend :-)

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

