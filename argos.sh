#!/usr/bin/env bash

URL="github.com/p-e-w/argos"
DIR=$(dirname "$0")

echo "Argos"
echo "---"
echo "$URL | iconName=help-faq-symbolic href='https://$URL'"
echo "$DIR | iconName=folder-symbolic href='file://$DIR'"
echo "get clipboard | bash='piknik -paste | xclip -selection c' terminal=false"
echo "send clipboard | bash='xclip -selection c -o | piknik -copy' terminal=false"


