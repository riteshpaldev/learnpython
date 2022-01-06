#!/bin/bash
if [ "$(id -u)" != "0" ]; then
  echo -e "\n${Yellow} This script must be run as root ${Color_Off}"
  echo -e "${Yellow} Try change to user root: sudo su -- or sudo su - userroot ${Color_Off}"
  echo -e "${Blue} sudo su -- or ${Color_Off}"
  echo -e "${Blue} sudo su - [root username] ${Color_Off}"
  echo -e "" 1>&2
  exit 1
fi






:
