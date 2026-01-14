@echo off
REM %~n0 获取当前bat文件名（不带扩展名），例如：wow.bat -> wow
cd /d "%~dp0.."
python run.py %~n0 %1
