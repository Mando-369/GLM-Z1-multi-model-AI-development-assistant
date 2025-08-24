#!/bin/bash
# Play sound when task completes
afplay /System/Library/Sounds/Glass.aiff
echo "Task completed at $(date)" >> doc/tasks/completion.log