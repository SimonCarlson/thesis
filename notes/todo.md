To do:

- [ ] Keep sketching header formats
- [ ] Expand/improve the presentation
- [x] Make sure the background of the thesis has a clear train of though (motivations for using these technologies - how do they solve problems occuring in IoT networks)
- [x] Make the introduction more fluent and explain the value in updating IoT devices remotely
- [x] Interconnecting book
  - [x] Chapter 8
  - [x] Chapter 9
  - [x] Chapter 11.2, 11.3
  - [x] Chapter 13
- [x] Reread and improve the introduction and background
- [ ] Consider adding section about CBOR
  - [ ] Talk to Niclas about state of CBOR in Contiki-NG
- [ ] Consider how to integrate EST-coaps into the mechanism
  - [x] Read EST RFC
  - [ ] Does it require anything from the application?
  - [ ] Does it change conditions for key management? How do keys reach the device? (Can use predistributed certificate to authenticate on EST server)
  - [x] Further explain why it is needed (from SUIT)
- [x] Fix presentation so that someone with no prior knowledge can understand what SUIT is
- [ ] Start looking at a minimal C manifest parser
- [ ] JSON to CBOR converter
  - [x] Create script that accepts version, vendor, class, device, and image that generates all mandatory fields
  - [x] Let script derive version, vendor, class, and device from an existing JSON manifest
  - [ ] Figure out how to sign it. If not EST, use whatever method for proof of concept
  - [x] Validate correctness of mandatory fields (using cbor.me perhaps?)
  - [ ] Figure out how to add options without making the entire thing clunky
- [ ] Rewrite the introduction regarding device management (architecture not implementation)
- [ ] Further push understanding of standardisation - needs flexibility, details left to implementation

