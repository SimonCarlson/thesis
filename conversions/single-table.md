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