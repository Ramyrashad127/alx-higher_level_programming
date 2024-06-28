#!/bin/bash
#display the body if success
HTTP_RESPONSE=$(curl -s -w "HTTPSTATUS:%{http_code}" -o /tmp/output "$1")
HTTP_BODY=$(cat /tmp/output)
HTTP_STATUS=${HTTP_RESPONSE##*HTTPSTATUS:}
if [ "$HTTP_STATUS" -eq 200 ]; then
    echo "$HTTP_BODY"
fi
rm /tmp/output
