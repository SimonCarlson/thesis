| Threat | Description                                                  | Threat Model                              | Mitigated By |
| ------ | ------------------------------------------------------------ | ----------------------------------------- | ------------ |
| MFT1   | Old Firmware                                                 | Elevation of Privilege                    | MFSR1        |
| MFT2   | Mismatched Firmware                                          | Denial of Service                         | MFSR2        |
| MFT3   | Offline device + old firmware                                | Elevation of Privilege                    | MFSR3        |
| MFT4   | The target device misinterprets the type of payload          | Denial of Service                         | MFSRa        |
| MFT5   | The target device installs the payload to the wrong location | Denial of Service                         | MFSR4b       |
| MFT6   | Redirection                                                  | Denial of Service                         | MFSR4c       |
| MFT7   | Payload Verification on Boot                                 | Elevation of Privilege                    | MFSR4d       |
| MFT8   | Unauthenticated Updates                                      | Elevation of Privilege                    | MFSR5        |
| MFT9   | Unexpected Precursor Image                                   | Denial of Service                         | MFSR4e       |
| MFT10  | Unqualified Firmware                                         | Denial of Service, Elevation of Privilege | MFSR6, MFSR8 |
| MFT11  | Reverse Engineering Of Firmware Image for Vulnerability Analysis | All classes                               | MFSR7        |
| MFT12  | Overriding Critical Manifest Elements                        | Elevation of Privilege                    | MFSR8        |

| Security Requirement | Description                            | Implemented By                               | Mitigates    |
| -------------------- | -------------------------------------- | -------------------------------------------- | ------------ |
| MFSR1                | Monotonic Sequence Numbers             | Monotonic Sequence Number                    | MFT1         |
| MFSR2                | Vendor, Device-type Identifiers        | Vendor ID Condition, Class ID Condition      | MFT2         |
| MFSR3                | Best-Before Timestamps                 | Best-Before timestamp condition              | MFT3         |
| MFSR4a               | Authenticated Payload Type             | Payload Format, Storage Location             | MFT4         |
| MFSR4b               | Authenticated Storage Location         | Storage Location                             | MFT5         |
| MFSR4c               | Authenticated Remote Resource Location | URIs                                         | MFT6         |
| MFSR4d               | Secure Boot                            | Payload Digest, Size                         | MFT7         |
| MFSR4e               | Authenticated precursor images         | Precursor Image Digest Condition             | MFT9         |
| MFSR4f               | Authenticated Vendor and Class IDs     | Vendor ID Condition, Class ID Condition      | MFT2         |
| MFSR5                | Cryptographic Authenticity             | Signature, Payload Digest                    | MFT8         |
| MFSR6                | Rights Require Authenticity            | Signature                                    | MFT10        |
| MFSR7                | Firmware Encryption                    | Content Key Distribution Method              | MFT11        |
| MFSR8                | Access Control Lists                   | Client-side code (not specified in manifest) | MFT10, MFT12 |

| Manifest Element                 | Status                               | Motivation/Notes                                             |
| -------------------------------- | ------------------------------------ | ------------------------------------------------------------ |
| Version identifier               | Mandatory                            | Describes the iteration of the manifest format               |
| Monotonic Sequence Number        | Mandatory                            | Prevents rollbacks to older images                           |
| Payload Format                   | Mandatory                            | Describes the format of the payload                          |
| Storage Location                 | Mandatory                            | Tells the device which component is being updated, can be used to establish physical location of update |
| Payload Digest                   | Mandatory                            | The digest of the payload to ensure authenticity. Must be possible to specify more than one payload digest indexed by XIP Address |
| XIP Address                      | -                                    | Used to specify which address the payload is for in systems with several potential images |
| Size                             | Mandatory                            | The size of the payload in bytes                             |
| Signature                        | Mandatory                            | The manifest is to be wrapped in an authentication container (not a manifest element itself) |
| Dependencies                     | Mandatory                            | A list of digest/URI pairs linking manifests that are needed to form a complete update |
| Precursor Image Digest Condition | Mandatory (for differential updates) | If a precursor image is required, this digest condition is needed |
| Content Key Distribution Method  | Mandatory (for encrypted payloads)   | Tells how keys for encryption/decryption are distributed     |
| Vendor ID Condition              | Recommended                          | Helps distinguish products from different vendors            |
| Class ID Condition               | Recommended                          | Helps distinguish incompatible devices in a vendors infrastructure |
|                                  |                                      |                                                              |
| Required Image Version List      | Optional                             | A list of versions that must be present to apply an update which applies to multiple versions of a firmware |
| Best-Before Timestamp Condition  | Optional                             | Tells the last application time                              |
| Component Identifier             | Optional                             | For heterogenous storages, identifies which part is to store the payload |
| URIs                             | Optional                             | A list of weighted URIs used to obtain the payload           |
| Directives                       | Optional                             | A list of instructions on processing the manifest. Applies to the entire manifest, unlike "Processing Steps" |
| Aliases                          | Optional                             | A list of digest/URI pairs                                   |
| Processing Steps                 | -                                    | A list of payload processors needed to process a nested format |
