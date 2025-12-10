#!/usr/bin/env bash
ps aux | grep Python | grep http.server && killall Python
./build.py > index.html
if [[ $BUILD_PID > 0 ]]; then
  >&2 echo "Build failed, exiting";
  exit;
fi;
python3 -m http.server -d ./web &
PY_PID=$!
open http://[::]:8000/index.html
sleep 5
kill $PY_PID