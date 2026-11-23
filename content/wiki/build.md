# Build the ISO

Use a disposable privileged **Arch Linux** container or Arch build host with several tens of GiB free. The scripts install build dependencies and require network access to Arch mirrors and the upstream SwayFX and Basedpyright releases.

```sh
pacman -Syu --needed archiso grub git python python-yaml shellcheck xfsprogs
bash tests/check.sh
bash scripts/build-repo.sh
mkarchiso -v -w /tmp/archiso-tmp -o /tmp/archiso-out .
PYTHONPATH="$PWD/airootfs/usr/share/arche/installer" python -P tests/guided-installer.py
```

Run these from the repository root. `build-repo.sh` builds and lints the repository's PKGBUILDs as an unprivileged user. SwayFX uses the upstream tagged source archive. Basedpyright uses its upstream npm release and Arch provides Bun. The builder verifies source checksums and indexes the resulting binary packages in `pkgs/local-repo/arche.db.tar.zst`. The empty optional CUDA metapackage validates its dependency transaction with `pacman -Sp --needed` and packages metadata with `makepkg --nodeps`, avoiding GPU-driver installation and DKMS execution on the builder. The default packages use full dependency installation. Root invocations create a temporary builder with passwordless sudo for pacman only; normal users use their existing sudo access. The builder and its sudoers rule are removed at exit, and the build host pacman configuration is restored. The build rewrites the `[arche]` stanza in the profile's `pacman.conf` to point at the generated local repository and generates the live image's corresponding configuration. Run it again after moving the checkout. Use fresh archiso work/output and package staging directories for each build; a nonempty package staging directory is rejected to prevent publishing stale artifacts.

The local repository contains unsigned packages built with the ISO and has a scoped `SigLevel = Optional TrustAll`; official Arch repositories continue to require signatures. The installer copies this repository into the target so its package sources remain accessible after reboot. Configure a signed release repository for future Arche package updates.
