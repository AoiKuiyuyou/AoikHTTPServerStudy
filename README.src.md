[:var_set('', """
# Compile command
aoikdyndocdsl -s README.src.md -n aoikdyndocdsl.ext.all::nto -g README.md
""")
]\
[:HDLR('heading', 'heading')]\
# AoikHTTPServerStudy
Python 2 **BaseHTTPServer** library and Python 3 **http.server** library study.

Tested working with:
- Python 2.7 and 3.5

Trace call using [AoikTraceCall](https://github.com/AoiKuiyuyou/AoikTraceCall):
- [BaseHTTPRequestHandlerTraceCall.py](/src/BaseHTTPRequestHandlerTraceCall.py)
- [BaseHTTPRequestHandlerTraceCallLogPy2.txt](/src/BaseHTTPRequestHandlerTraceCallLogPy2.txt?raw=True)
- [BaseHTTPRequestHandlerTraceCallLogPy3.txt](/src/BaseHTTPRequestHandlerTraceCallLogPy3.txt?raw=True)
- [BaseHTTPRequestHandlerTraceCallNotesPy2.txt](/src/BaseHTTPRequestHandlerTraceCallNotesPy2.txt?raw=True)
- [BaseHTTPRequestHandlerTraceCallNotesPy3.txt](/src/BaseHTTPRequestHandlerTraceCallNotesPy3.txt?raw=True)

## Table of Contents
[:toc(beg='next', indent=-1)]

## Set up AoikTraceCall
[:tod()]

### Setup via pip
Run:
```
pip install git+https://github.com/AoiKuiyuyou/AoikTraceCall
```

### Setup via git
Run:
```
git clone https://github.com/AoiKuiyuyou/AoikTraceCall

cd AoikTraceCall

python setup.py install
```

## Usage
[:tod()]

### Start server
Run:
```
python "AoikHTTPServerStudy/src/BaseHTTPRequestHandlerTraceCall.py" > Log.txt 2>&1
```

### Send request
Run:
```
curl -X POST -d hello http://127.0.0.1:8000/
```
