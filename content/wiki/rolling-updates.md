# Rolling updates

Arch mirrors provide the upstream system. The archelinux stable channel provides the distro packages. After the channel is active, update both with a full upgrade:

```sh
sudo pacman -Syu
```

The stable server is `https://raw.githubusercontent.com/archelinux/archelinux/rolling-channel/stable`. ISO release numbers identify installation media. Packages have their own versions. User-owned dotfiles remain yours when packaged templates change.

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

Future installation media ship the helper and key in `arche-maintenance`. The guided and unattended installers install from the bundled repository first and switch the target at the end. An ISO built before the first channel publication prints a message if the database has not been published. In that case run `sudo arche-enable-rolling` once the channel is available.

## Recovery

If an update fails signature verification, stop and retry a full upgrade after checking the system clock and network. The database and detached signature are separate HTTP requests. A client crossing a promotion can temporarily receive different revisions from a cache. Verification fails closed until both files match. Keep signature checks enabled. If a new package breaks a previously working setup, the alternate LTS boot entry, TTY2 and `sudo arche-rollback PACKAGE` are available according to the [recovery guide](recovery.html). Cached rollback needs the earlier archive and related packages may need coordinated downgrades.
