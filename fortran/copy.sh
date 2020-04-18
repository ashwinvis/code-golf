#!/bin/bash
echo "Copying minified source..."
mini=$(sed 's/ //g' $@)
echo "Word count (chars):"
echo "$mini" | wc --chars
printf "%s" "$mini" | head -n -1 | xclip -selection clipboard
echo "Done!"
