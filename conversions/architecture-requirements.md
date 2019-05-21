| Requirement                                     | Description                                                  |
| ----------------------------------------------- | ------------------------------------------------------------ |
| Agnostic to how firmware images are distributed | The mechanism should not assume a particular technology is used to distributed manifests and images, but instead be able to be carried over different mediums.This means decisions about formats and distribution methods must not rely on features of a particular technology. |
| Friendly to broadcast delivery                  | The mechanism should be broadcast friendly, meaning the mechanism can not be reliant on security on the transport layer or below. Also, devices receiving broadcast updates not meant for them should not incorrectly apply the update. |
| Use state-of-the-art security mechanisms        | The SUIT specification assumes a PKI is in place. The PKI allows for trusted communication. |
| Rollback attacks must be prevented              | The manifest should contain metadata such as monotonically increasing sequence numbers and best-before timestamps to avoid rollback attacks. |
| High reliability                                | The act of upgrading an image should not cause the device to break. This is an implementation requirement. |
| Operate with a small bootloader                 | The bootloader should be minimal. This is also an implementation requirement. |
| Small parser                                    | It must be easy to parse the fields of the update manifest as large parser can get quite complex. Validation of the manifest will happen on the constrained devices which further motivates a small parser and thus less complex manifests. |
| Minimal impact on existing firmware formats     | The update mechanism itself must not make assumptions of the current format of firmware images, but be able to support different types of firmware image formats. |
| Robust permissions                              | Updates must be authorized before they are applied, and different configurations might have different requirements for authorization. The architecture should enable a flexible and robust permission model. |
| Operating modes                                 | The draft presents three broad modes of updates: client-initiated updates, server-initiated updates, and hybrid updates, where hybrids are mechanisms that require interaction between the device and firmware provider before updating. The thesis will look into all three of these broad classes. Some classes may be preferred over others based on the technologies chosen in the thesis. |