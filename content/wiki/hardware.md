# Check your hardware after the first login

- On a laptop, suspend and resume once. Check that the lock screen appears and that Wi-Fi, audio and brightness controls still work after unlocking.
- If you use a dock, plug it in, unplug it and reconnect it. Run `swaymsg -t get_outputs` to see which displays Sway detects, then move a window between them and check the scale.
- Start a screen share in the browser or meeting app you actually use. Choose an output and confirm a second participant can see it.
- On a hybrid-GPU laptop, repeat the display and screen-sharing checks with the external monitor attached. If Sway fails to start, switch to TTY2 with Ctrl+Alt+F2 and log in to inspect the journal with `journalctl -b`.
