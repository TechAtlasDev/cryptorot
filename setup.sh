#!/bin/bash
clear

echo -e "\e[32m
  ____    ___   ______
 |    \  /   \ |      T
 |  D  )Y     Y|      |
 |    / |  O  |l_j  l_j
 |    \ |     |  |  |
 |  .  Yl     !  |  |
 l__j\_j \___/   l__j


\e[0m"

if ! command -v python3 &> /dev/null; then
    echo -e "\e[1;31m[\e[34m+\e[1;31m] \e[0mThis system requires Python 3 to be installed.\e[0m"
    exit 1
fi

current_directory=$(pwd)
echo "export PATH=\$PATH:$current_directory/src" >> ~/.bashrc
source ~/.bashrc

echo -e "\e[1;32m[\e[34m+\e[1;32m] \e[0mProcess finished, use the 'rot' command."
bash