@echo off
REM %~n0 获取当前bat文件名（不带扩展名），例如：auto.bat -> auto
REM 注意：auto 文件夹实际名称是 auto_mouse，run.py 会自动处理
cd /d "%~dp0.."
python run.py %~n0 %1
