@echo off
rem auto script run
cd /d "%~dp0.."
python run.py %~n0 %1
