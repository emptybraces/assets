@echo off
cd /d %~dp0
set TIME=%TIME: =0%
set TIME=%TIME::=%
set TIME=%TIME:~0,6%
set LOG_FILEPATH=%~dp0%DATE:/=%_%TIME%.log

rem process
rem call :ECHOES md folder
rem call :ECHOES dir
rem call :ECHOES echo this is test.
rem call :ECHOES cd folder
rem call :ECHOES sqlplus test/test@test test.sql
call :ECHOES echo testtt > test.txt
rem call :ECHOES2 echo testt test.txt

rem process end 
pause
exit

rem procedure
:ECHOES
	set _TMP=%~dp0tmp
	echo %cd%^> %* >> %LOG_FILEPATH%
	%* > %_TMP% 2>&1 
	type %_TMP%
	type %_TMP% >> %LOG_FILEPATH%
	del %_TMP%
	exit /b
:ECHOES2
	echo %cd%^> %1 %2 ^> %3>> %LOG_FILEPATH%
	exit /b