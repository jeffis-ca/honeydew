#!/bin/bash
mkdocs build -d ../honeydew-lib.github.io
cd ../honeydew-lib.github.io
git add -A .
git commit -m "docs"
git push -u origin master