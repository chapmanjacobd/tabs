#!/bin/bash
set -o xtrace         # print commands as they run
set -o errexit        # exit immediately if a pipeline returns a non-zero status
set -o errtrace       # trap ERR from shell functions, command substitutions, and commands from subshell
set -o nounset        # treat unset variables as an error
set -o pipefail       # pipe will exit with last non-zero status if applicable
# set -o noexec       # don't execute; only print
# set -o monitor      # job control is enabled
# set -o noclobber    # prevent output redirection using '>', '>&', '<>' from overwriting existing files

TABS=tabs_recent.txt
# TABS=tabs.txt

head -7 ~/d/00_Metadata/$TABS | xargs -n1 -t sh open
sed -i -e 1,7d ~/d/00_Metadata/$TABS
