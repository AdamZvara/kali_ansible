#!/bin/bash
/bin/bash -c "timeout 45 java -Djava.awt.headless=true -jar /usr/share/burpsuite/burpsuite.jar < <(echo y) &"
sleep 30
curl http://localhost:8080/cert -o /home/kali/cacert.der
exit