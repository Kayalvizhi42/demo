
#  -------------------------------------------------------------------------------------------------
#   Copyright (c) 2016-2025.  SupportVectors AI Lab
#   This code is part of the training material, and therefore part of the intellectual property.
#   It may not be reused or shared without the explicit, written permission of SupportVectors.
#
#   Use is limited to the duration and purpose of the training at SupportVectors.
#
#   Author: SupportVectors AI Training Team
#  -------------------------------------------------------------------------------------------------


#!/usr/bin/env python3
import sys
import os
import subprocess

DOCS_DIR = "docs"  # Change this if your docs are in a different folder

def generate_markdown(py_file):
    """Generate a Markdown documentation file for the given Python file."""
    filename = os.path.basename(py_file)
    module_name = os.path.splitext(filename)[0]
    md_file = os.path.join(DOCS_DIR, f"{module_name}.md")

    if not os.path.exists(md_file):
        print(f"📄 Generating documentation: {md_file}")
        os.makedirs(DOCS_DIR, exist_ok=True)
        
        # Run pydoc-markdown to generate docs
        with open(md_file, "w", encoding="utf-8") as f:
            subprocess.run(["pydoc-markdown", "--module", module_name], stdout=f, check=True)
    else:
        print(f"✅ Documentation already exists: {md_file}")

if __name__ == "__main__":
    files = [f for f in sys.argv[1:] if f.endswith(".py")]

    for py_file in files:
        generate_markdown(py_file)

    print("\n🎉 Documentation check complete!")
