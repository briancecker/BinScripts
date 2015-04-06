#!/bin/bash
RES=$($@)
echo "$RES" | tr -d "\n" | xclip -sel clip
