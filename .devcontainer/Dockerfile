# syntax=docker/dockerfile:1
FROM ubuntu:latest
# suppress clear apt cache
RUN rm -f /etc/apt/apt.conf.d/docker-clean; echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache

# install packages
ENV DEBIAN_FRONTEND=noninteractive

ENV LANG=ja_JP.UTF-8
#ENV LC_ALL=ja_JP.UTF-8
#ENV LC_CTYPE=ja_JP.UTF-8

ARG USERNAME=vscode
ARG UID=10000
ARG GID=$UID

# Remove user if already exist and create new user.
RUN set -eux; \
    if getent passwd "${UID}" > /dev/null; then \
    echo "UID ${UID} already exists. Deleting..."; \
    userdel -f $(getent passwd "${UID}" | cut -d: -f1) || true; \
    fi; \
    if getent group "${GID}" > /dev/null; then \
    echo "GID ${GID} already exists. Deleting..."; \
    groupdel $(getent group "${GID}" | cut -d: -f1) || true; \
    fi; \
    rm -rf /home/*; \
    groupadd --gid "${GID}" "${USERNAME}"; \
    useradd --uid "${UID}" --gid "${GID}" -s /bin/bash -m "${USERNAME}"

# enable sudo
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# APT Firefox
# Fixed to install from not snap but apt
# https://linux-jp.org/?p=5455

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update \
    && apt-get install --no-install-recommends -y \
    software-properties-common \
    && add-apt-repository -y ppa:mozillateam/ppa

# set up choose apt over snap
RUN cat <<EOF > /etc/apt/preferences.d/mozilla-firefox
Package: *
Pin: release o=LP-PPA-mozillateam
Pin-Priority: 1001

Package: firefox
Pin: version 1:1snap1-0ubuntu2
Pin-Priority: -1
EOF

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update \
    && apt-get install --no-install-recommends -y \
    git ssh \
    python3 python3-dev python3-venv python-is-python3 \
    firefox dbus-x11 fonts-noto-cjk

# COPY .devcontainer/init-docker-container.sh /usr/local/bin/init-docker-container.sh
# RUN chmod +x /usr/local/bin/init-docker-container.sh

# Minial Java
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update \
    && apt-get install --no-install-recommends -y \
    # Basic tools
    # ssh is required to handle GitHub in the container
    # git ssh \
    default-jdk-headless \
    # default-jdk \
    # required to install sdkman and gradle
    # Both zip and unzip are required to install.
    curl unzip zip \
    # System tools
    locales tzdata \
    # Configure locale
    && locale-gen ja_JP.UTF-8 \
    && update-locale LANG=ja_JP.UTF-8 \
    # Configure timezone
    && ln -fs /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata


# change user. Exec as vscode after this directive.
USER vscode

COPY requirements.txt .
ARG PIP_CACHE_DIR=/home/vscode/.cache/pip
RUN mkdir -p $PIP_CACHE_DIR
RUN --mount=type=cache,target=/home/vscode/.cache/pip,sharing=locked  \
    sudo chown vscode:vscode /home/vscode/.cache/pip \
    && python3 -m venv $HOME/venv \
    && $HOME/venv/bin/pip install --upgrade pip \
    && $HOME/venv/bin/pip install -r requirements.txt

# activate venv
RUN cat <<'EOF' >> /home/vscode/.bashrc

export LANG=$LANG

if [ -f "$HOME/venv/bin/activate" ] && [ -z "$VIRTUAL_ENV" ]; then
    . "$HOME/venv/bin/activate"
fi
EOF
