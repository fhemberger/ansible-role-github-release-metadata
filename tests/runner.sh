#!/usr/bin/env bash
set -euo pipefail

color_red='\033[0;31m'
color_green='\033[0;32m'
color_reset='\033[0m'

output=""

# TODO: Grab exit code. Script exit code = code | code

assert() {
  assertion="$1"
  result="$2"
  expected="$3"

  if [ "$result" = "$expected" ]; then
    output="$output\\n${color_green}[OK]\\t$assertion${color_reset}"
  else
    output="$output\\n${color_red}[ERROR]\\t$assertion\\t$(echo "$result" | tr '\n' ' ') - expected: $expected${color_reset}"
  fi;
}

assert "tests/args.json"           "$(python3 plugins/modules/github_release_metadata.py tests/args.json | jq '.status')"         "200"
assert "tests/args-with-tag.json" "$(python3 plugins/modules/github_release_metadata.py tests/args-with-tag.json | jq '.status')" "200"
assert "tests/args-404.json"      "$(python3 plugins/modules/github_release_metadata.py tests/args-404.json | jq '.failed')"      "true"

echo -e "$output" | column -t -s $'\t'
