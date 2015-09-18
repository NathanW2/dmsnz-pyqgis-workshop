@ECHO OFF
REM ---------------------------------------------------------------------------------------

REM Script to setup the environment for building Roam with QGIS 2.x.
REM This script sets the base folder that is used though out the build process
REM and sets the location to Python.

REM Change %OSGEO4W_ROOT% in setenv.bat to change in the location of QGIS.

REM ---------------------------------------------------------------------------------------



set OSGEO4W_ROOT=C:\OSGeo4W
SET QGISNAME=qgis
SET QGIS=%OSGEO4W_ROOT%\apps\%QGISNAME%
set QGIS_PREFIX_PATH=%QGIS%
SET PYCHARM="C:\Program Files (x86)\JetBrains\PyCharm Community Edition 4.0.2\bin\pycharm.exe"

CALL %OSGEO4W_ROOT%\bin\o4w_env.bat

set PATH=%PATH%;%QGIS%\bin;C:\Program Files (x86)\Git\bin
set PYTHONPATH=%QGIS%\python;%PYTHONPATH%

cd %~dp0
cmd