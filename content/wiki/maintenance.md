# Run local inference

Select Ollama or llama.cpp in **Arche software** to get a local runtime and archelinux's user-service definitions. The services start when you enable them, and you choose which models to download. On an existing system, install `arche-inference-defaults` alongside the runtime using the [rolling update guide](rolling-updates.html).

## Ollama

```sh
systemctl --user enable --now ollama.service
ollama list
```

Choose and pull a model that fits your hardware, then use `ollama run MODEL` with the model name. The service binds to loopback.

## llama.cpp

Save a model on disk and put `LLAMA_MODEL=/absolute/path/to/model.gguf` in `~/.config/arche/llama-server.env`. Then start the service:

```sh
systemctl --user enable --now llama-server.service
systemctl --user status llama-server.service
```

For startup errors, read `journalctl --user -u llama-server -n 40` and check the model path. To stop and disable a runtime, use `systemctl --user disable --now` with its service name. For NVIDIA compute, see the optional bundle in [Choose software](software.html).
