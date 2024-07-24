#!/bin/bash
(
export PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
REC_FILE="$1"
CALLER_ID="$2"
echo REC_FILE;
echo CALLER_ID
source venv/bin/activate
python main.py --caller_id "${CALLER_ID}" --audio_path "${REC_FILE}"
)&
disown -h
exit 0