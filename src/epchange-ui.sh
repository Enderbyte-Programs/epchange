#!/usr/bin/bash
epchange ui "$@"
#Execute UI mode, continuing to parse other things
exit $?
#Retain exit code