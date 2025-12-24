# Extension Cleanup Utility (Python)

A simple Python command-line tool to find and delete files by extension from a specified folder, with recursive search, a real-time progress bar, and logging support.

---

## Features

- Find files by extension (.tmp, .log, .txt, etc.)
- Optional recursive directory search
- Real-time CLI progress bar
- Safe file deletion with error handling
- Automatic logging to cleanup.log

---

## How It Works

1. Scans a folder for files matching a given extension
2. Deletes each file one by one
3. Displays a progress bar while deleting
4. Logs every deletion or error to cleanup.log

---

## Requirements

- Python 3.7 or higher
- No external dependencies (uses Python standard library only)

---
## Examples of use 
1. Delete `.txt` files in `del` (non-recursive):
```
python cleanup_tool.py del .txt
```
2. Delete recursively:
```
python cleanup_tool.py del .txt -r
```
3. Dry run (list only):
```
python cleanup_tool.py del .txt --dry
```

---

## License

The MIT License (MIT)
Copyright © 2025 DaveDrafts

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


