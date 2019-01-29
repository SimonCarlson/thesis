# Internet draft SUIT architecture

## Section 6

### Considerations for the device

Does it trust the author of the update? (PKI signing)

Has the firmware been corrupted? (Checksum of binary)

Does the firmware update apply to this device? (Metadata)

Is the update older than the active firmware? (Metadata)

When should the device apply the update? (Arbitrary?)

How should the device apply the update? (Hardware dependent)

What kind of firmware binary is it? (Metadata)

Where should the update be obtained? (Hard-coded server? Server discovery?)

Where should the firmware be stored? (Hardware dependent)

How does the device obtain the firmware? (Thinking CoAP observe pattern on manifest, issue GET request of firmware when manifest has been pushed)

### Contained in manifest

Information about the device(s) the firmwire image is intended to be applied to

Information about when the firmware update has to be applied

Information about when the manifest was created

Dependencies on other manifests

Pointers to the firmware image and information about the format

Information about where to store the firmware image

Cryptographic information, such as digital signatures or message authentication codes (MACs)