"© 2026 Punksm4ck. All rights reserved."
#!/bin/bash
    COORD=$(cat "$COORD_FILE")
    LAT=$(echo $COORD | cut -d"," -f1)
    LON=$(echo $COORD | cut -d"," -f2)
    URL="https://www.google.com/maps?q=$LAT,$LON"
    echo -e "\e[1;32m[OSIRIS LIVE FEED]\e[0m"
    echo "Coordinates: $LAT, $LON"
    echo -e "Map Link: \e[4;34m$URL\e[0m"
    # Surgical handoff to prevent exit errors
    nohup xdg-open "$URL" >/dev/null 2>&1 &
else
    echo -e "\e[1;31m[ERROR]\e[0m latest_coord.txt not found."
fi
