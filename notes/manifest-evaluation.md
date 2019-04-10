# Use cases

- Installation instructions

  - Can be included as directives in the options field

- Override non-critical manifest elements

  - The proposed manifest format has the critical elements as a baseline and the rest severed into the options field. Omitting options or defining new option types allows for new information.

- Modular update

  - Supported through precursor images, dependencies, and the use of authorization tokens for more granular updates.

- Multiple authorizations

  - Enforced via operator and update server whitelists and authorization tokens.

- Multiple payload formats

  - The architecture and manifest format does not make assumptions about the payload formats. The mappings of formats to integers in the manifest is deployment specific.

- Prevent confidential information disclosure

  - The architecture is based on state-of-the-art security mechanisms and suggests the use of strong algorithms such as ECC. Both manifest and payload are encrypted and authenticated.

- Prevent devices from unpacking unknown formats

  - Supported through the use of manifest format, overridable/custom directives, and letting the update server pick if there is a suitable update for a device matching against its registered profile

- Specify version numbers of target firmware

  - Devices register their version alongside vendor and class ID, meaning operators can query device statutes from the update server and then preparing updates matching these categories.

- Enable devices to choose between images

  - Several images can be included in a single manifest through the use of either precursors, dependencies, URIs (mirror list), or aliases depending on the specific use case. New options can also be defined capturing this behaviour, such as a new option providing URL/Digest pairs intended for parallel storage.

- Secure boot using manifests

  - % TODO: No idea about secure boot, have not looked into it whatsoever (scope?)

- Decompress on load

  - This behaviour can be encoded in the payload format of the manifest, or through the use of a custom option indicating a compressed payload is stored

- Payload in manifest

  - Can be added as the optional "payload" element, the value would be the data of the payload and the payloadInfo would contain its digest

- Simple parsing

  - The manifest format used is simple to parse even for embedded devices

  

