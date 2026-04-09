"© 2026 Punksm4ck. All rights reserved."
"© 2026 Punksm4ck. All rights reserved."
#!/bin/bash
URL="https://maps.google.com/maps?q=${LAT},${LON}&t=k"
echo -e "\e[1;32m[OSIRIS LIVE FEED]\e[0m"
echo "Coordinates: $LAT, $LON"
echo -e "Map Link: \e[4;34m$URL\e[0m"
xdg-open "$URL" &>/dev/null &
