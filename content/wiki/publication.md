# CI and package signing

## Installation images

The [ISO build](https://github.com/archelinux/archelinux/actions/workflows/build-iso.yml) builds the packages, assembles the image and exercises installation and desktop startup in a virtual machine. The release workflow signs the verified ISO and checksum from the same run. The [download page](../download/index.html) links the image and its verification files.

## Rolling packages

The [package workflow](https://github.com/archelinux/archelinux/actions/workflows/release-pkgs.yml) builds without signing credentials, then stages a signed snapshot. A VM installs the verified public 2.0.0 ISO, upgrades the installed desktop from the candidate, exercises a cached rollback, reapplies the upgrade and cold-boots the result. Promotion publishes the tested commit to the [rolling channel](https://github.com/archelinux/archelinux/tree/rolling-channel/stable). Existing installations keep the same server address across promotions.

For the first promotion, the project signed and tested the candidate locally. See the [rehearsal results](recovery.html). The published repository includes package archives, repository indexes, the bootstrap helper and detached signatures. The website verifies the release key and signed database before refreshing the [package directory](../packages/index.html). The [secondary mirror](mirrors.html) also verifies the individual package signatures.

If you’re setting up an installed machine, follow the [rolling update guide](rolling-updates.html). For the release operator procedure, see the [maintainer documentation](https://github.com/archelinux/archelinux/blob/main/docs/rolling-updates.md).
