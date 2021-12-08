# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.10, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.10-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
ARG VARIANT=3.7-bullseye
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

ENV PYTHONUNBUFFERED 1

RUN wget https://github.com/mvdan/sh/releases/download/v3.4.1/shfmt_v3.4.1_darwin_arm64 \
    -O /usr/local/bin/shfmt \
    && chmod +x /usr/local/bin/shfmt

RUN wget https://github.com/koalaman/shellcheck/releases/download/v0.8.0/shellcheck-v0.8.0.darwin.x86_64.tar.xz \
    -O- | tar xJ --strip-components=1 -C /usr/local/bin/ --wildcards '*/shellcheck' \
    && chmod +x /usr/local/bin/shellcheck 

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

# Starship.js prompt
RUN sh -c "$(curl -fsSL https://starship.rs/install.sh)" -- --force \
    && echo 'eval "$(starship init zsh)"' >> /home/vscode/.zshrc