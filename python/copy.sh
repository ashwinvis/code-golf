#!/bin/bash
echo "Copying minified source..."
mini=$(pyminifier --obfuscate-variables --obfuscate-classes --obfuscate-functions $@)
echo "Word count (chars):"
echo "$mini" | wc --chars
printf "%s" "$mini" | head -n -1 | xclip -selection clipboard
echo "Done!"
