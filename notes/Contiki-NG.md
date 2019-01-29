# Contiki-NG

## Repository Structure

- os contains all actual Contiki-NG code (processes, timers, networking stack, libraries, services). All examples compile and link to os.
- arch contains all hardware-dependant code (CPU, device, and platform drivers). This is where you put your code if porting Contiki-NG to a platform
- examples contains ready-to-use examples.
- tools contains tools which are not to be included in a Contiki-NG firmware (flashing tools, cooja, docker and vagrant scripts etc)
- tests contains all CI tests. They run in Travis for every pull request and merge.

## Build System

Resulting binary files includes both application and OS
A common Makefile is included in addition to the projects Makefile
Compile with TARGET=target and possibly BOARD for non-native applications

The firmware is always placed in <b>.</b>
Compilation output files and dependency files are found in <b>build/target/[board]/[build_dir_config]/obj</b>
Build configurations, if used, are found in <b>build/target/[board]/[build_dir_config]</b>

<b>clean</b> removes all build output files for the target, including <b>build/target/</b>.
<b>distclean</b> cleans all build output files for all targets and also deletes <b>build/</b>.

<b>make file_name.ramprof</b> and <b>make file_name.flashprof</b> to troubleshoot RAM and ROM sizes

## Configuration System

Modules, sub-directories of the top-level os directory, can be included in the Makefile variable MODULES.
The networking stack has two main layers, MAC and NET (network).
When using IPv6, you can also choose routing protocol through MAKE_ROUTING

To set other configuration parameters, create a <b>project-conf.h</b> inside the project directory. Make sure to <b>make distclean</b> after. A list of common flags can be found in <b>os/contiki-default-conf.h</b>.

## Logging System

The logging system works on a module level, with different log levels per module. The different log levels are disabled, errors, errors and warnings, errors, warnings and information logs, all of the above and debug messages.
<b>log-conf.h</b> shows the different modules currently supporting logging. Log levels can be set in a <b>project-conf.h</b> file.

