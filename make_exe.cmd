if exist "rpchm.spec" (
	python D:\Dev\pyinstaller-2.0\pyinstaller.py rpchm.spec
) else (
	python D:\Dev\pyinstaller-2.0\pyinstaller.py -y --onefile -r "HTML Help Workshop/hhc.exe",DATA,"HTML Help Workshop/hhc.exe" -r "HTML Help Workshop/itcc.dll",DATA,"HTML Help Workshop/itcc.dll" rpchm.py
)

pause

dim a.datas += [('HTML Help Workshop/hhc.exe', 'HTML Help Workshop/hhc.exe',  'DATA'),
dim ('HTML Help Workshop/itcc.dll', 'HTML Help Workshop/itcc.dll',  'DATA'),]