#!/bin/bash
# auto-save.sh
# Save all Krita files every 5 minutes automatically.

echo "🧠 Auto-save script started..."
while true; do
  find ~/Documents/KritaProjects -type f -name "*.kra" -mmin +5 -exec cp {} {}.bak \;
  echo "💾 Auto-saved at $(date '+%H:%M:%S')"
  sleep 300
done
