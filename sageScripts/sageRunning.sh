#!/bin/bash
if pgrep [s]age >/dev/null 2>&1
  then
     echo "Sage is running"
  else
     "Sage is not running"
fi
