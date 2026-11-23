# CI and package signing

`build-iso.yml` runs Docker explicitly on Ubuntu with `--privileged` and `/dev:/dev`, checks loop-device availability, and runs package build/lint, mkarchiso and runtime smoke tests. ISOs are written into the workspace `out/` directory for artifact upload. `release.yml` calls the build workflow, waits for the QEMU installation and desktop boot to pass, then signs the ISO from that run. `release-pkgs.yml` builds packages without signing secrets, then signs them in a separate `package-release` environment and publishes an immutable GitHub Release tag.

Configure these environment secrets before running package publication:

- `ARCHE_SIGNING_KEY`: ASCII-armored persistent private key.
- `ARCHE_SIGNING_FINGERPRINT`: signing key fingerprint.
- `ARCHE_SIGNING_PASSPHRASE`: key passphrase (empty for an unencrypted CI key).

Verify the published public key fingerprint through a trusted channel, import and locally sign it with `pacman-key`, then replace the local `[arche]` entry with:

```ini
[arche]
SigLevel = Required DatabaseRequired
Server = https://github.com/archelinux/archelinux/releases/download/pkgs-RUN_ID-RUN_ATTEMPT
```

Each immutable tag includes signed package archives, signed `arche.db` / `arche.files`, and the public key. Point clients at the new tag to adopt a later repository release. Both release workflows use a persistent release key. The required GitHub signing secrets must be configured before using CI for signing.
