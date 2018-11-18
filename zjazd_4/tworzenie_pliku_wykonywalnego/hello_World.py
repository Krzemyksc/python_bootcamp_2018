#Najpierw zrób pip install pyinstaller
import sys

if len(sys.argv) > 1:
    print("Hello", sys.argv[1])
else:
    print("Hello World")
# pyinstaller --onefile Hello_World.py jak skończysz to ta komenda


# dumps - zmień na tekst
#
# dump - chce plik
# load - chce plik