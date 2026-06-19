"""Convenience launcher: run the app straight from the project folder.

Usage: ``python main.py``. Prefers the installed package; falls back to the
``src/`` tree so it works without ``pip install``.
"""

# Mom's Canning Timer - Customizable stove top timers.
# Copyright (C) 2017-2026 willtheorangeguy

import os
import sys

try:
    from moms_canning_timer.app import main
except ModuleNotFoundError:
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))
    from moms_canning_timer.app import main

if __name__ == "__main__":
    main()
