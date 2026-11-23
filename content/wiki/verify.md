# Verify the ISO

Download the ISO, checksum, both signatures and release public key into a fresh directory. If the download is split, place all numbered parts together. Verify the signing-key fingerprint using a trusted source. Set `iso` to the ISO filename from the checksum file and run:

```sh
iso=$(awk 'NR == 1 { print $2 }' ./*.iso.sha256)
if [ ! -f "$iso" ]; then cat "$iso".part[0-9][0-9] > "$iso"; fi
gpg --show-keys --fingerprint archelinux-release-public.asc
gpg --import archelinux-release-public.asc
gpg --verify "$iso.sha256.sig" "$iso.sha256"
sha256sum -c "$iso.sha256"
gpg --verify "$iso.sig" "$iso"
```

Write the verified ISO to USB. Follow the [installation guide](installation.html) for the walkthrough.
