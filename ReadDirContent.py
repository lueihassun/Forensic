import os

folder = 'folderPath'
dateinamen = os.listdir(folder)
for dateiname in dateinamen:
    pfad = os.path.join(folder, dateiname)
    istordner = os.path.isdir(pfad)
    if istordner == 1:
        Info = 'Ordner:'
    else:
        Info = 'Datei:'
    print("%s %s" % (Info, pfad))
