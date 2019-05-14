| Requirement                            | Motivation                                                   |
| -------------------------------------- | ------------------------------------------------------------ |
| Monotonic sequence numbers             | The manifest contains monotonically increasing sequence numbers to prevent rollback attacks to older version of firmware. Signed manifests ensures an attacker cannot modify an old manifest to just update the sequence number and roll back the device firmware. |
| Vendor and device-type identifiers     | The thesis used nested UUID5 identifiers as vendor and device identifiers where the vendor UUID is the namespace for the device UUID. Implemented as preconditions in the manifest format. |
| Best-before timestamps                 | Can be added as an option or precondition.                   |
| Cryptographic authenticity             | Payloads are signed in COSE which ensures authenticity. The image digest is also calculated and checked against the digest in the manifest. |
| Authenticated payload type             | Payload format is mandatory, carried in the signed manifest. |
| Authenticated storage location         | Storage location is mandatory, carried in the signed manifest. |
| Authenticated remote resource location | URL is mandatory in the payloadInfo structure, carried in the signed manifest. |
| Secure boot                            | Information enabling secure boot such as image digest and size is included in the signed manifest. |
| Authenticated precursor images         | All precursors must have their URLs and digests included in the signed manifest. |
| Authenticated vendor and class IDs     | Both are implemented as preconditions in the signed manifest. |
| Rights require authenticity            | Exercising different rights can be achieved through the use of certificates (identity), whitelists (coarse-grained access control), and tokens (fine-grain access control). |
| Firmware encryption                    | All communication in the architecture is encrypted and the payloads are signed. Keys for encryption are handled through certificates and for signing through the content key method manifest element. |
| Access control lists                   | Access control is achieved through whitelists of operators and update servers and possibly tokens. |
| Encrypted manifests                    | All communication in the architecture is encrypted and signed. |