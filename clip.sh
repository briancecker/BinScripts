#!/bin/bash
RES=$($@)
echo "$RES" | xclip -sel clip
