#!/bin/bash
#echo "${date}" >> log.txt
echo 'shell' - "$(date +"%d-%m-%Y %H:%M:%S")" -- "$1" "$2" >> log.txt
#echo $2 >> log.txt
#echo $1 >> log.txt
(
export PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
REC_FILE="$2"
CALLER_ID="$1"
echo REC_FILE;
echo CALLER_ID
source venv/bin/activate
sleep 10
python main.py --caller_id "${CALLER_ID}" --audio_path "${REC_FILE}"
)&
disown -h
exit 0