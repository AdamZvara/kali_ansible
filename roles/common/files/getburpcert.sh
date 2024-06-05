#!/bin/bash

# Run burp suite
/bin/bash -c "timeout 95 java -Djava.awt.headless=true -jar /usr/share/burpsuite/burpsuite.jar < <(echo y) &"
sleep 30

# Get the certificate
curl http://localhost:8080/cert -o /home/kali/cacert.der
exit