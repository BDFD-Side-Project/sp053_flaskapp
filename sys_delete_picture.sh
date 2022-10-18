#!/bin/bash 
# Comment/NAME 20200422.2000hrs 
# Backup script 
rm -rf ~/../var/www/flaskapp/pichistory && mkdir ~/../var/www/flaskapp/pichistory

cd search
# Install dependencies for communicating with Meilisearch.
poetry install
# Set the same version as used for the docs
export MEILISEARCH_VERSION=0.27.1
# Set the right version for your operating system
# Replace the part after `meilisearch-`
# For macOS, use `macos-amd64`
# For Windows, use `windows-amd64.exe`
# For Linux, `linux-aarch64` is also available
export RELEASE_FILE=meilisearch-linux-amd64
# Download Meilisearch.
curl -OL "https://github.com/meilisearch/MeiliSearch/releases/download/v$MEILISEARCH_VERSION/$RELEASE_FILE"
# Make Meilisearch executable – skip for Windows, probably
mv "$RELEASE_FILE" "meilisearch"
chmod 744 "meilisearch"
# Set a master key.
export MEILI_MASTER_KEY=test
# Run it.
./meilisearch
cd ../docs
npm install
npm run dev
npm run build:search
hugo
# Export master key again in this terminal.
export MEILI_MASTER_KEY=test
./deploy.sh
cd ../search
# Update the index
./post_deploy.sh
cd ../docs
hugo serve