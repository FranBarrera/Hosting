;
; BIND data file for local loopback interface
;
$TTL    604800
@       IN      SOA     {{domain}}. root.{{domain}}. (
                              13         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL
;
@               IN      NS      hosting.{{domain}}.
$ORIGIN {{domain}}.
targaryen       IN      A       192.168.10.5
www				IN		CNAME	hosting
ftp				IN		CNAME	hosting
mysql			IN		CNAME	hosting
