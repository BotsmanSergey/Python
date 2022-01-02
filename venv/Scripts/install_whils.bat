@echo off

rem This file is UTF-8 encoded, so we need to update the current code page while executing it
for /f "tokens=2 delims=:." %%a in ('"%SystemRoot%\System32\chcp.com"') do (
    set _OLD_CODEPAGE=%%a
)
if defined _OLD_CODEPAGE (
    "%SystemRoot%\System32\chcp.com" 65001 > nul
)

set VIRTUAL_ENV=C:\Learning\Python\venv

if not defined PROMPT set PROMPT=$P$G

if defined _OLD_VIRTUAL_PROMPT set PROMPT=%_OLD_VIRTUAL_PROMPT%
if defined _OLD_VIRTUAL_PYTHONHOME set PYTHONHOME=%_OLD_VIRTUAL_PYTHONHOME%

set _OLD_VIRTUAL_PROMPT=%PROMPT%
set PROMPT=(venv) %PROMPT%

if defined PYTHONHOME set _OLD_VIRTUAL_PYTHONHOME=%PYTHONHOME%
set PYTHONHOME=

if defined _OLD_VIRTUAL_PATH set PATH=%_OLD_VIRTUAL_PATH%
if not defined _OLD_VIRTUAL_PATH set _OLD_VIRTUAL_PATH=%PATH%

set PATH=%VIRTUAL_ENV%\Scripts;%PATH%

:END
if defined _OLD_CODEPAGE (
    "%SystemRoot%\System32\chcp.com" %_OLD_CODEPAGE% > nul
    set _OLD_CODEPAGE=
)

pip install .\venv\wheels\bcrypt-3.2.0-cp36-abi3-win_amd64.whl
pip install .\venv\wheels\cffi-1.15.0-cp39-cp39-win_amd64.whl
pip install .\venv\wheels\cryptography-36.0.0-cp36-abi3-win_amd64.whl
pip install .\venv\wheels\paramiko-2.8.1-py2.py3-none-any.whl
pip install .\venv\wheels\pycparser-2.21-py2.py3-none-any.whl
pip install .\venv\wheels\PyNaCl-1.4.0-cp35-abi3-win_amd64.whl
pip install .\venv\wheels\six-1.16.0-py2.py3-none-any.whl
pause
