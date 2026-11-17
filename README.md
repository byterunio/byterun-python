# ByteRun Python SDK

The official Python SDK for [ByteRun](https://byterun.io/), an AI infrastructure platform that
provides execution environments for Python, SQL and AI agents.

> **Early preview.** Version `0.0.x` reserves the `byterun` package name and sets up the
> project. The SDK itself is **not ready yet**: it can't run anything today. In the meantime,
> try ByteRun in the [playground on byterun.io](https://byterun.io/), and follow the
> [roadmap](https://byterun.io/roadmap) for the first functional release.

## What is ByteRun?

ByteRun gives developers managed environments to run code and AI agents without operating the
infrastructure themselves. Today that covers Python, SQL and agent execution; the platform
roadmap also includes headless jobs, workflows and inference. See the
[platform overview](https://byterun.io/platform) for details.

## What this SDK is for

This SDK is meant to be the single Python entry point to ByteRun, so you can work with the
platform from your own code, scripts and services. AI agent execution comes first; other
platform capabilities will be added to the same package rather than split into separate ones.

What is planned, in no fixed order and subject to change: projects, code and agent execution,
files, SQL, headless jobs, workflows and inference. **None of this is available yet.**

## Installation

Requires Python 3.10 or newer.

```bash
pip install byterun
```

Check that it installed:

```bash
python -c "import byterun; print(byterun.__version__)"
```

The package currently exposes only `byterun.__version__`. API documentation and usage examples
will appear here once the client is released.

## Naming

| Where                  | Name             |
| ---------------------- | ---------------- |
| PyPI package           | `byterun`        |
| Python import          | `byterun`        |
| GitHub repository      | `byterun-python` |

## Feedback and contributions

Questions, ideas and bug reports are welcome as
[GitHub issues](https://github.com/byterunio/byterun-python/issues). The API is still being
designed, so please open an issue to discuss before sending a large pull request.

## Links

- Website: <https://byterun.io/>
- Platform: <https://byterun.io/platform>
- Roadmap: <https://byterun.io/roadmap>
- PyPI: <https://pypi.org/project/byterun/>
- Source: <https://github.com/byterunio/byterun-python>

## License

Licensed under the [Apache License, Version 2.0](LICENSE). Unless required by applicable law
or agreed to in writing, the software is distributed on an "AS IS" basis, without warranties or
conditions of any kind.
