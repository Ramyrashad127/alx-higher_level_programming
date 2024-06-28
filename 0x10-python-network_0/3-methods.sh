#!/bin/bash
#options
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-
