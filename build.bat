@echo off
echo ========================================
echo SAM PRO - Build Script
echo ========================================
echo.

echo Installing required packages...
pip install -r requirements.txt

echo.
echo Cleaning previous builds...
if exist "dist" rmdir /s /q "dist"
if exist "build" rmdir /s /q "build"
if exist "__pycache__" rmdir /s /q "__pycache__"

echo.
echo Building executable...
pyinstaller sam_pro.spec

echo.
if exist "dist\SAM_PRO.exe" (
    echo ========================================
    echo Build completed successfully!
    echo Executable location: dist\SAM_PRO.exe
    echo ========================================
    echo.
    echo Testing the executable...
    echo Press any key to test the application...
    pause >nul
    start "" "dist\SAM_PRO.exe"
) else (
    echo ========================================
    echo Build failed!
    echo Please check the error messages above.
    echo ========================================
)

echo.
echo Press any key to exit...
pause >nul
