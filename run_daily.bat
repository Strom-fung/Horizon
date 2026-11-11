@echo off
chcp 65001 >nul
set PATH=%PATH%;C:\Users\iceco\AppData\Roaming\Python\Python311\Scripts
set PYTHONIOENCODING=utf-8

cd /d E:\news\horizon

echo ============================================
echo  Horizon Daily Run - %date% %time%
echo ============================================

horizon --hours 48

echo.
echo Done: %date% %time%
