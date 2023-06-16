hyprpaper_path="/home/hodes/.config/hypr/hyprpaper.conf"
current_bg="/home/hodes/wallpapers/current.txt"
# Temporarily store the remaining lines of hyprpaper.conf file
tmp=$(mktemp)

# Write the new content to the first line of hyprpaper.conf file
echo "preload = $(cat $current_bg)" > "$tmp"
echo "wallpaper = eDP-1, $(cat $current_bg)" >> "$tmp"
tail -n +3 "$hyprpaper_path" >> $tmp
# Append the remaining lines back to hyprpaper.conf file
mv "$tmp" "$hyprpaper_path"
