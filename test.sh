#!/bin/env bash
set -euo pipefail

pytest -vv

python -m dinject README.md docs/examples.md
