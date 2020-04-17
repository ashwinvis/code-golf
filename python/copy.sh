#!/bin/bash
echo "Copying minified source..."
mini=$(pyminifier --obfuscate-variables $@)
echo "Word count (chars):"
echo $mini | wc -c
echo $mini | xclip -selection clipboard
echo "Done!"
