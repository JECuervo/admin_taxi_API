cd ..
@echo off
if not exist "venv" (
    virtualenv venv
    call venv\Scripts\activate.bat
    pip install -r admin_taxi_api\requirements.txt
) else (
    echo "Entorno virtual existente"
)
pause
exit