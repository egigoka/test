
PROFILE_PATH=$(find ~/.mozilla/firefox/ -maxdepth 1 -type d -name "*.default-release" -print -quit)
SESSION_FILE="${PROFILE_PATH}/sessionstore-backups/recovery.jsonlz4"

if [ -f "$SESSION_FILE" ]; then
    echo "Found session file: $SESSION_FILE"
    lz4jsoncat "$SESSION_FILE" | jq -r '.windows[].tabs[] | .entries[].url'
else
    echo "Session file not found at $SESSION_FILE"
    echo "Ensure Firefox is closed or check for the correct profile and session file name."
fi
