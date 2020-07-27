#!/usr/bin/env bash
set -euo pipefail

readonly ANSIBLE_COLLECTION_DIR="ansible_collections/github/test"

# sanity tests *require* this directory structure
mkdir -p "$ANSIBLE_COLLECTION_DIR/plugins/modules"
cp -r "$GITHUB_WORKSPACE/plugins/modules" "$ANSIBLE_COLLECTION_DIR/plugins"
cd "$ANSIBLE_COLLECTION_DIR"

# sanity tests *require* a .git directory
git init

# sanity test 'validate-modules' *requires* a GPL3 comment
find . -name "*.py" -exec sed -i 's|# MIT License|# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)|' {} +

ansible-test sanity --python 3.8
