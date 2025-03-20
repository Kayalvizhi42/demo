
import sys
import os

# Define the copyright text
COPYRIGHT = """
#  -------------------------------------------------------------------------------------------------
#   Copyright (c) 2016-2025.  SupportVectors AI Lab
#   This code is part of the training material, and therefore part of the intellectual property.
#   It may not be reused or shared without the explicit, written permission of SupportVectors.
#
#   Use is limited to the duration and purpose of the training at SupportVectors.
#
#   Author: SupportVectors AI Training Team
#  -------------------------------------------------------------------------------------------------
"""

# Get staged Python files
staged_files = os.popen("git diff --cached --name-only --diff-filter=A | grep '.py$'").read().splitlines()

for file in staged_files:
    with open(file, "r+", encoding="utf-8") as f:
        content = f.read()
        if "Copyright" not in content:
            # Prepend the copyright notice
            f.seek(0, 0)
            f.write(COPYRIGHT + "\n\n" + content)
    
    # Re-add the modified file to staging
    os.system(f"git add {file}")

sys.exit(0)