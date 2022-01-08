cd %~dp0
%~dp0
set /p aab=aab_path:
java -jar bundletool.jar build-apks --connected-device --bundle=%aab% --output=myapp.apks
java -jar bundletool.jar install-apks --apks=myapp.apks
java -jar bundletool.jar extract-apks --apks=myapp.apks --output-dir=./my.apks --device-spec=sanxing.json
del myapp.apks