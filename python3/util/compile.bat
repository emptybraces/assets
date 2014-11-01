
:remove compiled file
rmdir __pycache__ /s /q
:compile
..\python -m compileall util.py

:rename
cd __pycache__
for /f "tokens=1-3 delims=. usebackq" %%a in (`dir /b`) do (
    ren %%a.%%b.%%c %%a.%%c
)
cd ..\

:copy
copy __pycache__\util.pyc ..\..\..\collada_utility\dae_convert\
copy __pycache__\util.pyc ..\

pause