@echo ON

:: Use custom profile to build GCC on Windows
set PROFILE_ARGS=-pr profiles/msys2
:: Configure the terminal to run bash.exe
set MSYSTEM=MSYS
set MSYS2_PATH_TYPE=inherit
set CHERE_INVOKING=1


echo "** INSTALL MSYS2 CONAN PACKAGE **"
CALL conan install -r conancenter --requires=msys2/cci.latest -g VirtualBuildEnv
if %ERRORLEVEL% neq 0 goto ERROR_EXIT


echo "** ACTIVATE CONAN BUILD ENVIRONMENT **"
CALL conanbuild.bat
if %ERRORLEVEL% neq 0 goto ERROR_EXIT

echo "** START MSYS2 BASH TERMINAL AND BUILD THE AUTOTOOLSTOOLCHAIN EXAMPLE **"
CALL %MSYS_BIN%\bash.exe -lc ./run_example.sh
if %ERRORLEVEL% neq 0 goto ERROR_EXIT

exit /b 0

:ERROR_EXIT
    echo "ERROR: Could not execute the example with success."
    exit /b %ERRORLEVEL%
