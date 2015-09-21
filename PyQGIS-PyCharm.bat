@ECHO OFF

REM Update this path to point to your QGIS install
set OSGEO4W_ROOT=C:\OSGeo4W
SET QGISNAME=qgis
SET QGIS=%OSGEO4W_ROOT%\apps\%QGISNAME%
set QGIS_PREFIX_PATH=%QGIS%

REM Update this path to point to your PyCharm install
SET PYCHARM="C:\Program Files (x86)\JetBrains\PyCharm Community Edition 4.0.2\bin\pycharm.exe"

CALL %OSGEO4W_ROOT%\bin\o4w_env.bat

set PATH=%PATH%;%QGIS%\bin;
set PYTHONPATH=%QGIS%\python;%PYTHONPATH%

start "PyCharm aware of QGIS" /B %PYCHARM% %*