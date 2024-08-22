from pathlib import Path
import sys
import os

app_directory = os.path.dirname(sys.argv[0])

def check_resource_path():
    path = Path(app_directory, 'resource')
    if not path.exists():
        path.mkdir(parents = True)
    return "Complete"

def check_data_path():
    path = Path(app_directory, 'resource/data')
    if not path.exists():
        path.mkdir(parents = True)
    return True

def check_diagnostic_path():
    path = Path(app_directory, 'resource/diagnostic')
    if not path.exists():
        path.mkdir(parents = True)
    return True

