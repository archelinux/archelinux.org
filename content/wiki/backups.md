# Back up files and settings

Use a separate drive or backup destination so a disk failure or reinstall leaves a copy you can reach. Include project files, documents and photos, along with the [configuration files](configuration.html) you want to keep. Repositories may have untracked work, so a remote Git push only covers what was committed and pushed.

## Save a copy before an update or reinstall

Mount your separate destination using the [removable drive guide](storage.html). Check the mount point and available space.

```sh
findmnt --mountpoint /path/to/backup
df -h /path/to/backup
```

This example writes a tar archive outside your home directory. Replace the example paths and select an unused archive name. Consider the size of downloads, local models and VM images before archiving all of your home.

```sh
tar -czf /path/to/backup/home-YYYY-MM-DD.tar.gz -C "$HOME" .
tar -tzf /path/to/backup/home-YYYY-MM-DD.tar.gz | less
```

Protect the destination if it contains private keys, credentials or browser data. Keep another copy of files you cannot replace.

## Check that you can restore

Pick a small file from the archive listing and extract it into a temporary directory. Use its exact listed name in place of `./Documents/example.txt`.

```sh
restore_dir=$(mktemp -d)
tar -xzf /path/to/backup/home-YYYY-MM-DD.tar.gz -C "$restore_dir" ./Documents/example.txt
cmp "$HOME/Documents/example.txt" "$restore_dir/Documents/example.txt"
```

No output from `cmp` means the two files match. Check recovered files before copying them over current versions. For an update that breaks a package, use [package recovery](recovery.html).
