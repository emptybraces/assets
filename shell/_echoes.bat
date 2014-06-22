@echo off
cd /d %~dp0
set TIME=%TIME: =0%
set TIME=%TIME::=%
set TIME=%TIME:~0,6%
set LOG_FILEPATH=%~dp0%DATE:/=%_%TIME%.log

rem process
call :ECHOES md folder
call :ECHOES dir
call :ECHOES echo this is test.
call :ECHOES cd folder
call :ECHOES sqlplus test/test@test test.sql
rem call :ECHOES echo test > test.txt


rem process end 
pause
exit

rem procedure
:ECHOES
	set _TMP=%~dp0tmp
	set _OUTPUT=%*
	echo %cd%^> %_OUTPUT% >> %LOG_FILEPATH%
	%* > %_TMP% 2>&1 
	type %_TMP%
	type %_TMP% >> %LOG_FILEPATH%
	del %_TMP%
	exit /b
