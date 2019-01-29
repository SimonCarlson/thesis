# Internet draft SUIT information model

## Section 1

"The information model does not define the encoding (CBOR?), ordering, or structure of information elements, only their semantics."

"Because the information model covers a wide range of user stories and a wide range of threats, not all information elements apply to all scenarios. As a result, many information elements could be considered optional to implement and optional to use, depending on which threats exist in a particular system and which use cases are required." It is imperative to identify threats and use cases for the particular software and firmware updates the thesis discusses in order to formulate a complete yet not redundant information model based on SUIT.

## Section 3

### STRIDE classes (covers only transport issues)

Spoofing identity

Tampering with data

Repudiation

Information disclosure

Denial of service

Elevation of privilege

### Threat descriptions

- MFT1: Old Firmware
  - Elevation of Privilege
  - An old but valid manifest with an old but valid firmware is sent, downgrade to known vulnerability
  - Mitigated by MFSR1
- MFT2: Mismatched Firmware
  - Denial of Service
  - Valid firmware for wrong device type
  - Mitigated by MFSR2
- MFT3: Offline device + old firmware
  - Elevation of Privilege
  - An offline device with old firmware is sent a old, but newer than current, firmware with known vulnerabilities.
  - Mitigated by MFSR3
- MTF4: The target device misinterprets the type of payload
  - Denial of Service
  - Firmware might be installed incorrectly
  - Mitigated by MFSR4a
- MFT5: The target device installs the payload to the wrong location
  - Denial of Service
  - If a firmware image is installed to the wrong location it is likely to fail.
  - Mitigated by MFSR4b
- MFT6: Redirection
  - Denial of Service
  - A device might be redirected to an attacker's server if it does not know where to get the firmware.
  - Mitigated by MFSR4c
- MFT7: Payload Verification on Boot
  - Elevation of Privilege
  - A newly downloaded firmware can be replaced after it's manifest has been verified.
  - Mitigated by MFSR4d
- MFT8: Unauthenticated Updates
  - Elevation of Privilege
  - If an unauthenticated attacker can install their firmware they have full control of the device.
  - Mitigated by MFSR5
- MFT9: Unexpected Precursor Image
  - Denial of Service
  - A device is sent a valid, current manifest with an unexpected precursor image.
  - Mitigated by MFSR4e
- MFT10: Unqualified Firmware
  - Denial of Service, Elevation of Privilege
  - If the firmware is not qualified it might cause breakage due to interoperability issues.
  - Mitigated by MFSR6, MFSR8
- MFT11: Reverse Engineering Of Firmware Image for Vulnerability Analysis
  - All classes
  - A valid firmware image is reverse engineered by an attacker for vulnerability analysis
  - Mitigated by MFSR7
- MFT12: Overriding Critical Manifest Elements
  - Elevation of Privilege
  - An authorised actor (different from the firmware authority) can override information elements in a manifest already signed by the firmware authority.
  - Mitigated by MFSR8

### Security Requirements

- MFSR1: Monotonic Sequence Numbers
  - Manifests MUST contain monotonically increasing sequence numbers. Devices MUST reject manifests with sequence numbers smaller than any onboard sequence number.
  - Mitigates MFT1
  - Implemented by Manifest Element: Monotonic Sequence Number
- MFSR2: Vendor, Devicy-type Identifiers
  - Devices MUST only apply firmware that is intended for them. Unique identifiers SHOULD be used.
  - Mitigates MFT2
  - Implemented by Manifest Elements: Vendor ID Condition, Class ID Condition
- MFSR3: Best-Before Timestamps
  - Firmware MAY expire. Devices with secure clocks MUST reject the manifest if current time is larger than the best-before time.
  - Mitigates MFT3
  - Implemented by: Manifest Element: Best-Before timestamp condition
- MFSR4a: Authenticated Payload Type
  - The type of payload MUST be authenticated (types could be firmware, loadable modules, configuration data etc)
  - Mitigates MFT4
  - Implemented by Manifest Elements: Payload Format, Storage Location
- MFSR4b: Authenticated Storage Location
  - The location on the device MUST be authenticated.
  - Mitigates MFT5
  - Implemented by Manifest Element: Storage Location
- MFSR4c: Authenticated Remote Resource Location
  - The location where a payload can be found MUST be authenticated
  - Mitigates MFT6
  - Implemented by: Manifest Element: URIs
- MFSR4d: Secure Boot
  - The target SHOULD verify firmware at time of boot
  - Mitigates MFT7
  - Implemented by Manifest Elements: Payload Digest, Size
- MFSR4e: Authenticated precursor images
  - If an update uses a differential compression method, it MUST specify the digest of the precursor image and that digest MUST be authenticated
  - Mitigates MFT9
  - Implemented by Manifest Elements: Precursor Image Digest Condition
- MFSR4f: Authenticated Vendor and Class IDs
  - Identifiers specifying firmware compability MUST be authenticated
  - Mitigates MFT2
  - Implemented by Manifest Elements: Vendor ID Condition, Class ID Condition
- MFSR5: Cryptographic Authenticity
  - The updates and manifest must be digitally authenticated. Manifest contains the digest of the firmware image, the authenticity of the manifest can be verified with a digital signature or MAC.
  - Mitigates MFT8
  - Implemented by: Signature, Payload Digest
- MFSR6: Rights Require Authenticity
  - Different rights granted by a device to different actors MUST require proof when trying to exercise those rights.
  - Mitigates MFT10
  - Implemented by: Signature
- MFSR7: Firmware Encryption
  - The manifest must convey the information required to allow an intended recipient to decrypt an encrypted payload
  - Mitigates MFT11
  - Implemented by Manifest Element: Content Key Distribution Method
- MFSR8: Access Control Lists
  - Access of different rights by different actors must be validated against a list of rights for the actor (such as an Access Control List [ACL])
  - Mitigates MFT10, MFT12
  - Implemented by: Client-side code, not specified in manifest

### Usability Requirements

- MFUR1: It must be possible to provide all information necessary for the processing of a manifest into the manifest
- MFUR2: It must be possible to redirect payload fetches. 
- MFUR3: It must be possible to express the requirement to install one or more payloads from one or more authorities.
- MFUR4: It MUST be possible to sign a manifest multiple times.
- MFUR5: The manifest format MUST accommodate any payload format that an operator wishes to use.
- MFUR6: The manifest format must accommodate nested formats.
- MFUR7: The manifest format must provide a method to specify multiple version numbers of firmware to which the manifest applies.
- MFUR8: The manifest format must provide a mechanism to list multiple equivalent payloads by Execute-In-Place Installation Address.

## Section 4

### Manifest Information Elements

- Version identifier of the manifest structure
  - An identifier that describes which iteration of the manifest format is contained in the structure
  - MANDATORY
- Monotonic Sequence Number
  - A monotonically increasing sequence number. For example, UTC timestamp
  - MANDATORY
  - Implements MFSR1
- Vendor ID Condition
  - Vendor IDs MUST be unique. Recommended practice is to use typ 5 UUIDs with the vendor's domain name and the UUID DNS prefix, this UUID is guaranteed to be unique. Because the domain name is known, this UUID is reproducible. Example: vendorId = UUID5(DNS, "vendor-a.com")
  - OPTIONAL but RECOMMENDED
  - Implements MFSR2, MFSR4f
- Class ID Condition
  - Class Identifiers MUST be unique within a Vendor ID. Recommended practice is to use type 5 UUIDs with the model, hardware revision, etc and use the Vendor ID as the UUID prefix. Classes MAY be implemented in a more granular way, but MUST NOT be implemented in a less granular way.
  - OPTIONAL but RECOMMENDED
  - Implements MFSR2, MFSR4f
- Precursor Image Digest Condition
  - When a precursor image is required by the payload format, a precursor image digest condition MUST be present in the conditions list.
  - MANDATORY for differential updates. Otherwise, it is not needed.
  - Implements MFSR4e
- Required Image Version List
  - The required image version list specifies which firmware versions must be present for the update to be applied.
  - OPTIONAL
  - Implements MFUR7
- Best-Before timestamp condition
  - This element tells a device the last application time.
  - OPTIONAL and MAY enable use cases where a secure clock is provided and firmware is intended to expire regularly.
  - Implements MFSR3
- Payload format
  - The format of the payload must be indicated to devices in an unambiguous way.
  - MANDATORY and MUST be present
  - Implements MFSR4a, MFUR5
- Processing Steps
  - A list of all payload processors necessary to process a nested format. Each Processing Step SHOULD indicate the expected digest of the payload after processing is complete.
  - Implements MFUR6
- Storage Location
  - This element tells the device which component is being updated. The device can use this to establish which permission are necessary and the physical location to use.
  - MANDATORY and MUST be present.
  - Impements MFSR4b
- Component Identifier
  - A component identifier indicates which part of a heterogenous storage architecture is targeted by the payload.
  - OPTIONAL, only necessary in heterogeneous storage architecture devices.
  - Implements MFUR3
- URIs
  - This element is a list of weighted URIs that the device uses to select where to obtain a payload
  - OPTIONAL, only needed when the target device does not know where to find the payload
  - Implements MFSR4c
- Payload Digest
  - Contains the digest of the payload. It is used to ensure the authenticity of the payload. It MUST be possible to specify more than one payload digest, indexed by Manifest Element: XIP Address
  - MANDATORY
  - Implements MFSR4d, MFUR8
- Size
  - The size of the payload in bytes.
  - MANDATORY
  - Implements MFSR4d
- Signature
  - This is not a manifest element, but the manifest is wrapped by a standardised authentication container. The container MUST support multiple actors and authentications.
  - MANDATORY
  - Implements MFSR5, MFSR6, MFUR6
- Directives
  - A list of instructions that the device should execute in order when processing the manifest. It applies to the whole manifest, not just payloads (as Processing Steps does)
  - OPTIONAL
  - Implements MFUR1
- Aliases
  - A list of digest/URI pairs. A device should build an alias table while parsing a manifest tree and treat any aliases as top-ranked URIs for the corresponding digest.
  - OPTIONAL
  - Implements MFUR2
- Dependencies
  - A list of Digest/URI pairs. The manifests that are linked must be acquired and installed simultaneously.
  - MANDATORY
  - Implements MFUR3
- Content Key Distribution Method
  - The manifest contains an element for the Content Key Distribution Method since several methods to protect symmetric content encryption keys exist. En example is the usage of Key Tables.
  - MANDATORY for encrypted payloads
  - Implements MFSR7
- XIP Address
  - It is necessary to specify which address the payload is linked for.
  - Implements MFUR8