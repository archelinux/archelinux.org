# Recovery and local inference

Use the [installation guide](installation.html) for the current console ISO and the earlier published image. The former unattended XFS installer is exercised by the [legacy boot test](qemu.html).

Use the LTS boot entry when Zen fails after an update. Use `sudo arche-rollback PACKAGE` for a cached older package. Reflink workspaces can be created with `cp -a --reflink=always SOURCE DESTINATION` on the same XFS filesystem.

Inference is opt-in, with no models downloaded:

```sh
sudo pacman -S ollama
systemctl --user enable --now ollama.service
# Alternatively install llama.cpp, set LLAMA_MODEL to an absolute GGUF path in
# ~/.config/arche/llama-server.env, then enable llama-server.service.
```

Both servers bind to loopback. User units normally stop at logout; enable lingering explicitly if desired. For supported NVIDIA hardware, choose `arche-cuda` in the installer or run `sudo pacman -S arche-cuda` after installation.
