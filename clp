#!/bin/bash
tmux copy-mode && tmux send-keys -X cursor-up && tmux send-keys -X cursor-up && tmux send-keys -X cursor-up && tmux send-keys -X cursor-up && tmux send-keys -X cursor-up && tmux send-keys -X cursor-up && tmux send-keys -X cursor-up && tmux send-keys -X cursor-up && tmux send-keys -X cursor-up && tmux send-keys -X select-line && tmux send-keys -X cursor-down && tmux send-keys -X cursor-down && tmux send-keys -X cursor-down && tmux send-keys -X cursor-down && tmux send-keys -X cursor-down && tmux send-keys -X cursor-down && tmux send-keys -X cursor-down && tmux send-keys -X copy-selection-and-cancel

MATCHED_OUTPUT=$(pbpaste | grep -Eo "$1.*") 
LINES_OF_OUTPUT=$(echo "$MATCHED_OUTPUT" | wc -l | sed 's/ //g')
if [[ "$LINES_OF_OUTPUT" == "1" ]]; then
    echo "$MATCHED_OUTPUT" | tr -d '\n' | pbcopy
else
    echo "$MATCHED_OUTPUT" | enum | pbcopy
fi
