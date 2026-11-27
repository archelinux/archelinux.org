# Verify the ISO

Download the image, checksum manifest, both signatures and public key for the same release into a fresh directory. If the download is split, put all numbered parts in that directory. Run the commands below from a Bash shell with GnuPG, `gpgv` and `sha256sum`.

Check the fingerprint against the [release announcement](../news/index.html) or another trusted copy of the key. The pinned archelinux release fingerprint is **E446 C26A 0B7B A1A6 6A3D CC9F 7EC5 6400 3573 C80B**.

```bash
(
  set -euo pipefail
  work=$(mktemp -d)
  trap 'rm -rf -- "$work"' EXIT
  signer=E446C26A0B7BA1A66A3DCC9F7EC564003573C80B
  gpg --homedir "$work" --batch --import archelinux-release-public.asc
  gpg --homedir "$work" --batch --export "$signer" > "$work/release.gpg"
  test -s "$work/release.gpg"

  manifests=(./*.iso.sha256)
  test "${#manifests[@]}" -eq 1
  manifest=${manifests[0]}
  gpgv --homedir "$work" --keyring "$work/release.gpg" "$manifest.sig" "$manifest"
  iso=$(awk 'NR == 1 { print $2 }' "$manifest")
  if [ ! -f "$iso" ]; then
    cat "$iso".part[0-9][0-9] > "$iso"
  fi
  sha256sum -c "$manifest"
  gpgv --homedir "$work" --keyring "$work/release.gpg" "$iso.sig" "$iso"
)
```

Expect a good signature for both files and `OK` from `sha256sum`. If any check fails, download the complete set of files for the same release and retry. After verification, follow [Prepare a bootable USB or VM](install-media.html).
