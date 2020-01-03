# ja_pyinstaller
pyinstaller compile example
---

## Example

---

- Faire pyinstaller avec une icon:

pyinstaller -p /Users/johnny_hung/.game_simulation/lib/python3.6/site-packages -p /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6 --onefile --windowed --icon=ja.icns --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' run_lott.py


---

