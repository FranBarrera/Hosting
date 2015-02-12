;
; BIND data file for local loopback interface
;
$TTL    604800
@       IN      SOA     franbarrera.gonzalonazareno.org. root.franbarrera.gonzalonazareno.org. (
                              13         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL
;
@               IN      NS      targaryen.franbarrera.gonzalonazareno.org.
                        MX      10 baratheon.franbarrera.gonzalonazareno.org.
$ORIGIN franbarrera.gonzalonazareno.org.
maquina       IN      A       ip
