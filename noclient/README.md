## NoPen
noclient/noserver TAO tooling.

#### Usage
```
# keying instructions
./genkey ./key
./addkey.py -k ./key -p ./client.bin
./addkey.py -k ./key ./server.bin

# -help menu for client
NO! osboxes:/>-help
[07-27-23 22:24:42 GMT][localhost:37352 -> osboxes.127.0.0.1:32754]
[-help]

Remote General Commands:
Usage: -elevate 
Usage: -getenv 
Usage: -gs category|filename [options-if-any]
Usage: -setenv VAR=[val]
Usage: -shell [alt_shell]
Usage: -status 
Usage: -time 
Usage: -ps [options]
  select: -p pid1,pid2,... -q ppid1,ppid2,... -g gpid1,gpid2,...
          -n user1,user2,... -u uid1,uid2,...
          -t "ddMmmyy hh:mm"|yyyymmddhhmm|epoch
  sort:   -P  -Q   -G   -N   -U  -T     -V
          pid ppid gpid user uid time   inverse
  grep:   -r regex [-v] [-i]
  show uid: -I
  show last 24hrs: -d
  tree view: -H

Remote Server Commands:
Usage: -burn 
Usage: -call toip toport
Usage: -listen port
Usage: -pid 

Remote Network Commands:
Usage: -icmptime target_ip [source_ip] 
Usage: -ifconfig 
Usage: -nslookup name1 ...
Usage: -ping -r remote_target_ip [-l local_source_ip] [-i|-u|-t] [-p dest_port] [-s src_port]
       -ping host
       -ping [-u|-t|-i] host
Usage: -trace -r remote_target_ip [-l local_source_ip] [-i|-u|-t] [-p dest_port] [-s src_port]
       -trace host
       -trace [-u|-t|-i] host

Remote Redirection Commands:
Usage: -irtun target_ip call_back_port|RHP [listen_ip] [ourtn arguments]
Usage: -istun target_ip call_in_port|RHP [srcip] [ourtn arguments]
Usage: -jackpop target_ip target_port source_ip source_port
Usage: -nrtun [listenip:]port [fromip]
Usage: -nstun toip [toport [localport [srcport [srcip]]]]
       -nstun toip:port [srcip]
Usage: -rawsend [-s] tcp_port
Usage: -rtun [listenip:]port [toip [toport]] [fromip]
Usage: -rutun [listenip:]port [toip [toport]]
Usage: -scan [scan_name|port] [targetip]
Usage: -sentry target_address source_address (tcp|udp) dest_port src_port interface
Usage: -stun toip toport [localport [srcport [srcip]]]
Usage: -sutun toip toport [localport [srcport [srcip]]]
Usage: -tunnel [command_listen_port [udp|tcp [autoclose]]]
Usage: -vscan  (should add help)

Remote File Commands:
Usage: -cat remfile
Usage: -chili [-l] [-s lines] [-m max] MM-DD-YYYY remdir remfile [remfile ...]
Usage: -cksum remfile ...
Usage: -fget [MM-DD-YYYY] loclist
Usage: -get [-l] [-q] [-v] [-s minimumsize] [-m MM-DD-YYYY] remfile ...
Usage: -grep [-d] [-v] [-n] [-i] [-h] [-C number_of_context_lines] pattern file1 [file2 ...] 
Usage: -oget [-a] [-q] [-s skipoff] [-b begoff] [-e endoff] remfile
Usage: -put locfile remfile [mode]
Usage: -strings remfile
Usage: -tail [+/-n] remfile, + to skip n lines of remfile beginning
Usage: -touch [-t mtime:atime | refremfile] remfile
Usage: -rm remfile|remdir ...
Usage: -upload file port [fromip]
Usage: -mailgrep [-l] [-m maxbytes] [-r "regexp" [-v]] [-f regexpfilename [-v]] [-a "regexp for attachments to eliminate"] [-b MM-DD-YYYY] [-e MM-DD-YYYY] [-d remotedumpfile] remotedir file1 [file2 ...]
 ex: -mailgrep -a ".doc" -r "^Fred" -b 2-28-2002 /var/spool/mail G*

Remote Directory Commands:
Usage: -find [-d] [-M | -m -mkfindsargs] [-x[m|a|c] MM-DD-YYYY] remdir [remdir...]
Usage: -ls [-1ihuRt] [-x[m|a|c] MM-DD-YYYY] [remfile|remdir ...]
Usage: -cd [remdir]
Usage: -cdp 

Local Client Commands:
Usage: -autopilot port [xml]
Usage: -cmdout [locfilename]
Usage: -exit 
Usage: -help 
Usage: -hist 
Usage: -keepalive [-d] [-r] [[-v] interval]
Usage: -readrc [locfile]
Usage: -remark [comment]
Usage: -rem [comment]
Usage: # [comment]
Usage: -reset 

Local Environment Commands:
Usage: -lcd locdir
Usage: -lgetenv 
Usage: -lpwd 
Usage: -lsetenv VAR=[val]
Usage: -lsh [[-q] command]

Aliases:

NO! osboxes:/>
```

### Client (noclient)
```
noclient-3.0.3.6-i586.pc.linux.gnu:           ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.2.5, stripped
noclient-3.0.4.1-i586.pc.linux.gnu:           ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.2.5, stripped
noclient-3.0.5.3-i686.pc.linux.gnu.redhat-ES: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.2.5, stripped
noclient-3.1.0.2-i686.pc.linux.gnu.redhat-ES: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.2.5, stripped
noclient-3.1.0.5-i686.pc.linux.gnu.redhat-ES: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.2.5, stripped
noclient-3.3.2.3-linux-i386:                  ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.2.5, stripped

```
### Server component (NoServer)
```
noserver-3.0.3.4-i386.pc.bsdi-2.1:                          386 compact demand paged pure executable
noserver-3.0.4.1-alphaev6.dec.osf-4.0f:                     COFF format alpha demand paged executable dynamically linked stripped - version 0.0-2
noserver-3.0.4.1-alphaev67.unknown.linux.gnu.redhat-7.0:    ELF 64-bit LSB executable, Alpha (unofficial), version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.0.0, stripped
noserver-3.0.4.1-i386.pc.sco3.2v-5.0.5:                     ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /usr/lib/libc.so.1, stripped
noserver-3.0.4.1-i386.pc.solaris-2.6:                       ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /usr/lib/ld.so.1, stripped
noserver-3.0.4.1-i386.unknown.freebsd-4.3-static:           ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), statically linked, for FreeBSD 4.3, stripped
noserver-3.0.4.1-i386.unknown.freebsd-4.3:                  ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), dynamically linked, interpreter /usr/libexec/ld-elf.so.1, for FreeBSD 4.3, stripped
noserver-3.0.4.1-i386.unknown.freebsd-4.4-static:           ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), statically linked, for FreeBSD 4.4, stripped
noserver-3.0.4.1-i386.unknown.freebsd-4.4:                  ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), dynamically linked, interpreter /usr/libexec/ld-elf.so.1, for FreeBSD 4.4, stripped
noserver-3.0.4.1-i386.unknown.freebsd-4.5-static:           ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), statically linked, for FreeBSD 4.5, stripped
noserver-3.0.4.1-i386.unknown.freebsd-4.5:                  ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), dynamically linked, interpreter /usr/libexec/ld-elf.so.1, for FreeBSD 4.5, stripped
noserver-3.0.4.1-i386.unknown.freebsd-6.0-static:           ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), statically linked, stripped
noserver-3.0.4.1-i386.unknown.freebsd-6.0:                  ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), dynamically linked, interpreter /libexec/ld-elf.so.1, stripped
noserver-3.0.4.1-i386.unknown.openbsd-3.4-static:           ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), statically linked, for OpenBSD, stripped
noserver-3.0.4.1-i386.unknown.openbsd-3.4:                  ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /usr/libexec/ld.so, for OpenBSD, stripped
noserver-3.0.4.1-i386.unknown.openbsd-3.7-static:           ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), statically linked, for OpenBSD, stripped
noserver-3.0.4.1-i386.unknown.openbsd-3.7:                  ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /usr/libexec/ld.so, for OpenBSD, stripped
noserver-3.0.4.1-i586.pc.linux.gnu.redhat-5.0-static:       ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), statically linked, stripped
noserver-3.0.4.1-i586.pc.linux.gnu.redhat-5.0:              ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, stripped
noserver-3.0.4.1-i686.pc.linux.gnu.redflag-2.0:             ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.0.0, stripped
noserver-3.0.4.1-i686.pc.linux.gnu.redhat-ES:               ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.2.5, stripped
noserver-3.0.4.1-i686.pc.linux.gnulibc1.slackware-4.0.0:    ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.1, stripped
noserver-3.0.4.1-i686.pc.linux.gnuoldld.redhat-6.0:         ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.0.0, stripped
noserver-3.0.4.1-mips.sgi.irix-5.3:                         ELF 32-bit MSB executable, MIPS, MIPS-I version 1 (SYSV), dynamically linked, interpreter /usr/lib/libc.so.1, stripped
noserver-3.0.4.1-powerpc.ibm.aix-4.3.3.0:                   executable (RISC System/6000 V3.1) or obj module
noserver-3.0.4.1-sparc.sun.solaris-2.3:                     ELF 32-bit MSB executable, SPARC, version 1 (SYSV), dynamically linked, interpreter /usr/lib/ld.so.1, stripped
noserver-3.0.4.1-sparc.sun.solaris-2.4:                     ELF 32-bit MSB executable, SPARC, version 1 (SYSV), dynamically linked, interpreter /usr/lib/ld.so.1, stripped
noserver-3.0.4.1-sparc.sun.solaris-2.5.1:                   ELF 32-bit MSB executable, SPARC, version 1 (SYSV), dynamically linked, interpreter /usr/lib/ld.so.1, stripped
noserver-3.0.4.1-sparc.sun.solaris-2.5:                     ELF 32-bit MSB executable, SPARC, version 1 (SYSV), dynamically linked, interpreter /usr/lib/ld.so.1, stripped
noserver-3.0.4.1-sparc.sun.solaris-2.7:                     ELF 32-bit MSB executable, SPARC, version 1 (SYSV), dynamically linked, interpreter /usr/lib/ld.so.1, stripped
noserver-3.0.4.1-sparc.unknown.linux.gnu.redhat-6.2-static: ELF 32-bit MSB executable, SPARC, version 1 (SYSV), statically linked, for GNU/Linux 2.0.0, stripped, too many notes (256)
noserver-3.0.4.1-sparc.unknown.linux.gnu.redhat-6.2:        ELF 32-bit MSB executable, SPARC, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.0.0, stripped
noserver-3.0.4.2-armv5b.linux-static:                       ELF 32-bit MSB executable, ARM, version 1 (ARM), statically linked, for GNU/Linux 2.4.3, stripped
noserver-3.0.4.3-mips.linux:                                ELF 32-bit LSB executable, MIPS, MIPS32 version 1 (SYSV), statically linked, stripped
noserver-3.0.4.4-i386.mac:                                  Mach-O i386 executable, flags:<NOUNDEFS|DYLDLINK|TWOLEVEL>
noserver-3.0.5.3-hppa2.0w.hp.hpux-11.00:                    PA-RISC1.1 shared executable dynamically linked
noserver-3.0.5.3-i386.pc.solaris-2.6:                       ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /usr/lib/ld.so.1, stripped
noserver-3.0.5.3-i386.unknown.freebsd-4.7-static:           ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), statically linked, for FreeBSD 4.7, stripped
noserver-3.0.5.3-i386.unknown.freebsd-4.7:                  ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), dynamically linked, interpreter /usr/libexec/ld-elf.so.1, for FreeBSD 4.7, stripped
noserver-3.0.5.3-i386.unknown.freebsd-5.1:                  ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), dynamically linked, interpreter /usr/libexec/ld-elf.so.1, for FreeBSD 5.1, stripped
noserver-3.0.5.3-i386.unknown.freebsd-6.1:                  ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), dynamically linked, interpreter /libexec/ld-elf.so.1, stripped
noserver-3.0.5.3-i386.unknown.freebsd-7.0:                  ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), dynamically linked, interpreter /libexec/ld-elf.so.1, for FreeBSD 7.0 (700055), stripped
noserver-3.0.5.3-i686.pc.linux.gnu.redhat-5.0-static:       ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), statically linked, stripped
noserver-3.0.5.3-i686.pc.linux.gnu.redhat-5.0:              ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, stripped
noserver-3.0.5.3-i686.pc.linux.gnu.redhat-6.0:              ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.0.0, stripped
noserver-3.0.5.3-i686.pc.linux.gnu.redhat-ES:               ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.2.5, stripped
noserver-3.0.5.3-powerpc.ibm.aix-5.1:                       executable (RISC System/6000 V3.1) or obj module
noserver-3.0.5.3-sparc.sun.solaris-2.6:                     ELF 32-bit MSB executable, SPARC, version 1 (SYSV), dynamically linked, interpreter /usr/lib/ld.so.1, stripped
noserver-3.1.0.1-hppa2.0w.hp.hpux-11.00:                    PA-RISC1.1 shared executable dynamically linked
noserver-3.1.0.1-i386.apple.darwin-10.1:                    Mach-O i386 executable, flags:<NOUNDEFS|DYLDLINK|TWOLEVEL|NO_HEAP_EXECUTION>
noserver-3.1.0.1-i386.pc.solaris-2.6:                       ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /usr/lib/ld.so.1, stripped
noserver-3.1.0.1-i386.pc.solaris-2.8:                       ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /usr/lib/ld.so.1, stripped
noserver-3.1.0.1-i386.unknown.freebsd-4.7-static:           ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), statically linked, for FreeBSD 4.7, stripped
noserver-3.1.0.1-i386.unknown.freebsd-4.7:                  ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), dynamically linked, interpreter /usr/libexec/ld-elf.so.1, for FreeBSD 4.7, stripped
noserver-3.1.0.1-i386.unknown.freebsd-5.1:                  ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), dynamically linked, interpreter /usr/libexec/ld-elf.so.1, for FreeBSD 5.1, stripped
noserver-3.1.0.1-i386.unknown.freebsd-6.1:                  ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), dynamically linked, interpreter /libexec/ld-elf.so.1, stripped
noserver-3.1.0.1-i386.unknown.freebsd-7.0:                  ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), dynamically linked, interpreter /libexec/ld-elf.so.1, stripped
noserver-3.1.0.1-i686.pc.linux.gnu.redhat-5.0-static:       ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), statically linked, stripped
noserver-3.1.0.1-i686.pc.linux.gnu.redhat-5.0:              ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, stripped
noserver-3.1.0.1-i686.pc.linux.gnu.redhat-6.0:              ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.0.0, stripped
noserver-3.1.0.1-i686.pc.linux.gnu.redhat-ES:               ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.2.5, stripped
noserver-3.1.0.1-powerpc.ibm.aix-5.1:                       executable (RISC System/6000 V3.1) or obj module
noserver-3.1.0.1-sparc.sun.solaris-2.6:                     ELF 32-bit MSB executable, SPARC, version 1 (SYSV), dynamically linked, interpreter /usr/lib/ld.so.1, stripped
noserver-3.1.0.1-sparc.sun.solaris-2.8:                     ELF 32-bit MSB executable, SPARC32PLUS, V8+ Required, total store ordering, version 1 (SYSV), dynamically linked, interpreter /usr/lib/ld.so.1, stripped
noserver-3.1.0.5-hppa2.0w.hp.hpux-11.00:                    PA-RISC1.1 shared executable dynamically linked
noserver-3.1.0.5-i386.apple.darwin-10.4:                    Mach-O i386 executable, flags:<NOUNDEFS|DYLDLINK|TWOLEVEL|NO_HEAP_EXECUTION>
noserver-3.1.0.5-i386.pc.solaris-2.6:                       ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /usr/lib/ld.so.1, stripped
noserver-3.1.0.5-i386.pc.solaris-2.8:                       ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /usr/lib/ld.so.1, stripped
noserver-3.1.0.5-i386.unknown.freebsd-4.7-static:           ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), statically linked, for FreeBSD 4.7, stripped
noserver-3.1.0.5-i386.unknown.freebsd-4.7:                  ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), dynamically linked, interpreter /usr/libexec/ld-elf.so.1, for FreeBSD 4.7, stripped
noserver-3.1.0.5-i386.unknown.freebsd-5.1:                  ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), dynamically linked, interpreter /usr/libexec/ld-elf.so.1, for FreeBSD 5.1, stripped
noserver-3.1.0.5-i386.unknown.freebsd-6.1:                  ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), dynamically linked, interpreter /libexec/ld-elf.so.1, stripped
noserver-3.1.0.5-i386.unknown.freebsd-7.0:                  ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), dynamically linked, interpreter /libexec/ld-elf.so.1, stripped
noserver-3.1.0.5-i686.pc.linux.gnu.redhat-5.0-static:       ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), statically linked, stripped
noserver-3.1.0.5-i686.pc.linux.gnu.redhat-5.0:              ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, stripped
noserver-3.1.0.5-i686.pc.linux.gnu.redhat-6.0:              ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.0.0, stripped
noserver-3.1.0.5-i686.pc.linux.gnu.redhat-ES:               ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.2.5, stripped
noserver-3.1.0.5-powerpc.ibm.aix-5.1:                       executable (RISC System/6000 V3.1) or obj module
noserver-3.1.0.5-sparc.sun.solaris-2.6:                     ELF 32-bit MSB executable, SPARC, version 1 (SYSV), dynamically linked, interpreter /usr/lib/ld.so.1, stripped
noserver-3.1.0.5-sparc.sun.solaris-2.8:                     ELF 32-bit MSB executable, SPARC32PLUS, V8+ Required, total store ordering, version 1 (SYSV), dynamically linked, interpreter /usr/lib/ld.so.1, stripped
noserver-3.3.0.1-junos-8.4-and-below-i386:                  ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), for FreeBSD 4.4, dynamically linked, interpreter /usr/libexec/ld-elf.so.1, no section header
noserver-3.3.0.1-junos-8.5-and-above-i386:                  ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), dynamically linked, interpreter /usr/libexec/ld-elf.so.1, no section header
noserver-3.3.0.1-junos-ppc:                                 ELF 32-bit MSB executable, PowerPC or cisco 4500, version 1 (SYSV), dynamically linked, interpreter /usr/libexec/ld-elf.so.1, no section header
noserver-3.3.2.1-linux-ppc-static:                          ELF 32-bit MSB executable, PowerPC or cisco 4500, version 1 (SYSV), statically linked, no section header
noserver-3.3.2.3-aix-ppc:                                   executable (RISC System/6000 V3.1) or obj module
noserver-3.3.2.3-darwin_10-i386:                            Mach-O i386 executable, flags:<NOUNDEFS|DYLDLINK|TWOLEVEL>
noserver-3.3.2.3-darwin_11-i386:                            Mach-O i386 executable, flags:<NOUNDEFS|DYLDLINK|TWOLEVEL|PIE|NO_HEAP_EXECUTION>
noserver-3.3.2.3-darwin_9-i386:                             Mach-O i386 executable, flags:<NOUNDEFS|DYLDLINK|TWOLEVEL>
noserver-3.3.2.3-freebsd_4.7-i386-static:                   ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), for FreeBSD 4.7, statically linked, no section header
noserver-3.3.2.3-freebsd_4.7-i386:                          ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), for FreeBSD 4.7, dynamically linked, interpreter /usr/libexec/ld-elf.so.1, no section header
noserver-3.3.2.3-freebsd_5.0-i386:                          ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), for FreeBSD 5.0 (500043), dynamically linked, interpreter /usr/libexec/ld-elf.so.1, no section header
noserver-3.3.2.3-freebsd_6.0-i386:                          ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), dynamically linked, interpreter /libexec/ld-elf.so.1, no section header
noserver-3.3.2.3-freebsd_7.0-i386:                          ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), for FreeBSD 7.0 (700055), dynamically linked, interpreter /libexec/ld-elf.so.1, no section header
noserver-3.3.2.3-freebsd_8.0-i386:                          ELF 32-bit LSB executable, Intel 80386, version 1 (FreeBSD), for FreeBSD 8.0 (800107), dynamically linked, interpreter /libexec/ld-elf.so.1, no section header
noserver-3.3.2.3-hpux-hppa2_0:                              PA-RISC1.1 shared executable dynamically linked
noserver-3.3.2.3-linux-i386-static:                         ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), for GNU/Linux 2.2.5, statically linked, no section header
noserver-3.3.2.3-linux-i386:                                ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), for GNU/Linux 2.2.5, dynamically linked, interpreter /lib/ld-linux.so.2, no section header
noserver-3.3.2.3-linux-mipseb-static:                       ELF 32-bit MSB executable, MIPS, MIPS32 version 1 (SYSV), statically linked, no section header
noserver-3.3.2.3-linux-x86_64:                              ELF 64-bit LSB executable, x86-64, version 1 (SYSV), for GNU/Linux 2.4.1, dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, no section header
noserver-3.3.2.3-solaris_2.7-i386:                          ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /usr/lib/ld.so.1, no section header
noserver-3.3.2.3-solaris_2.7-sparc:                         ELF 32-bit MSB executable, SPARC, version 1 (SYSV), dynamically linked, interpreter /usr/lib/ld.so.1, no section header
noserver-3.3.2.3-solaris_2.8-i386:                          ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /usr/lib/ld.so.1, no section header
noserver-3.3.2.3-solaris_2.8-sparc:                         ELF 32-bit MSB executable, SPARC, version 1 (SYSV), dynamically linked, interpreter /usr/lib/ld.so.1, no section header
noserver-3.3.2.4-linux-i386-static:                         ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), for GNU/Linux 2.2.5, statically linked, no section header
noserver-3.3.2.4-linux-i386:                                ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), for GNU/Linux 2.2.5, dynamically linked, interpreter /lib/ld-linux.so.2, no section header
noserver-3.3.2.5-darwin-ppc:                                Mach-O ppc executable, flags:<NOUNDEFS|DYLDLINK|TWOLEVEL>

```

#### References
- **NOPEN** Backdoor? A RAT or post-exploitation shell consisting of a client and a server that encrypts data using RC6 [source](http://electrospaces.blogspot.nl/p/nsas-tao-division-codewords.html)**
- https://github.com/x0rz/EQGRP