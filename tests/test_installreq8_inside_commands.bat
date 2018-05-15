internal\test_installreq8_internal_remove_dependecies.py
FOR /D %%X IN (%LocalAppData%\Temp\pip-uninstall-*) DO RD /S /Q "%%X"
internal\test_installreq8_internal_check_import_dependencies.py
pause