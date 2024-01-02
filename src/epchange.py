#!/usr/bin/python3
import sys
import os

if os.path.isdir("/usr/lib/epchange"):
    sys.path.insert(0,"/usr/lib/epchange")

import epappdata
import cursesplus

args = sys.argv[1:]
if args[0] == "--help" or args[0] == "help":
    print("===== EPCHANGE HELP =====")
    print("usage: epchange [help|cmd|ui|-c [command]]")
    print("By default, if no args are provided, cmd mode will be started")
    print("UI mode is user-friendly. To get that, run epchange-ui instead of just epchange")