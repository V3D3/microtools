forcext: a minimal, extensible test case loader for programming websites

base version: receives requests from codeforces pages

### Setup:
- load `extension` into Chrome using unpacked extension option
- allow `codeforces.com` to run insecure content
- autostart `serv.py` or add alias in `bashrc` for easy startup:
```
    alias forces='nohup /path/to/serv.py > /dev/null &'
```

### Customization for your use:
1. Add regexes in `extension/content_script.js` and domain in `extension/manifest.json`.
2. Add test scraper in the same files.
3. Change editor opening code in `serv.py`.
4. Change testcase save pattern in `serv.py`.

### My usage:
1. Regexes supplied.
2. Scraping supplied.
3. Commands supplied (in vscode opens dir, opens file, additional customization: set `integrated.terminal.cwd` to `${fileDirname}` and use `Ctrl+Shift+(backtick)` to open terminal)
4. Pattern supplied (ease of indexing from bash).

5. Refer `runz` that resides in `/media/hdd/work/forces`, and is run from contest folders as pwd, in the form `../runz A` where A is the problem ID.