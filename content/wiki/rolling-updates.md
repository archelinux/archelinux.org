# Rolling updates

Arch mirrors provide upstream packages. Signed stable supplies the archelinux packages. For a routine update, review [Arch Linux news](https://archlinux.org/news/) for any manual steps, then update the system as a single transaction.

```sh
sudo pacman -Syu
```

The stable server is `https://raw.githubusercontent.com/archelinux/archelinux/rolling-channel/stable`. ISO release numbers identify installation media. Packages have their own versions. Review the transaction before confirming. If a kernel was updated, reboot when convenient so the running kernel matches the installed version. An update refreshes installed packages. To install an optional tool during the same transaction, add its package name, for example `sudo pacman -Syu worktrunk`. Use `pacman -Q worktrunk` to confirm it is installed.

Keep the rest of the system current when adding packages. Refreshing the databases alone with `pacman -Sy` and installing individual updates later can mix incompatible versions. Keep a [backup](backups.html) of your files and settings.

## Enabling stable on an existing 2.0.0 installation

Use the public release key you verified when you installed. If you need a new copy, obtain it from the signed ISO release and independently check the fingerprint **E446 C26A 0B7B A1A6 6A3D CC9F 7EC5 6400 3573 C80B**. Use the following commands in a shell with Bash syntax, replacing the key path with your own. A failed check stops the transition.

```bash
(
  set -euo pipefail
  key=/path/to/archelinux-release-public.asc
  server=https://raw.githubusercontent.com/archelinux/archelinux/rolling-channel/stable
  signer=E446C26A0B7BA1A66A3DCC9F7EC564003573C80B
  work=$(mktemp -d)
  trap 'rm -rf "$work"' EXIT
  gpg --homedir "$work" --batch --import "$key"
  gpg --homedir "$work" --batch --export "$signer" > "$work/release.gpg"
  test -s "$work/release.gpg"
  curl -fLSs "$server/arche-enable-rolling" -o "$work/enable"
  curl -fLSs "$server/arche-enable-rolling.sig" -o "$work/enable.sig"
  gpgv --homedir "$work" --keyring "$work/release.gpg" "$work/enable.sig" "$work/enable"
  sudo python "$work/enable" --key "$work/release.gpg"
)
```

The helper verifies the signed database against the pinned key, locally signs that key in pacman's keyring, and replaces the `[arche]` section in place. It leaves the Arch mirror configuration alone. The setup refuses an active pacman database lock. It can be run again after pacman finishes. Now run the full upgrade above. Check `pacman-conf --repo arche Server` and `pacman -Si arche/arche-maintenance` to see the selected server and package version.

Current netinstall images already configure stable. See [Install archelinux](installation.html) for the USB walkthrough.

If you used the earlier `rolling-20261123` image, it tried to enable stable at the end of setup. If that image kept its bundled repository because the channel was unreachable, run `sudo arche-enable-rolling` after connecting, followed by `sudo pacman -Syu`.

## Diagnose update errors

Check failed mirrors and package signatures before retrying. Use [network diagnostics](networking.html) if the hostname or connection fails. If pacman reports a lock, wait for any active package manager to finish. For a suspected stale lock after an interrupted update, inspect running processes and [pacman troubleshooting](https://wiki.archlinux.org/title/Pacman#Troubleshooting).

If an update fails signature verification, stop and retry a full upgrade after checking the system clock and network. The database and detached signature are separate HTTP requests. A client crossing a promotion can temporarily receive different revisions from a cache. Verification fails closed until both files match. Keep signature checks enabled. If a new package breaks a previously working setup, follow [Recover from a broken update](recovery.html).
