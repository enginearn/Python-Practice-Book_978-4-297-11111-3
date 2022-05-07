import re
import sys

def py2_or_py3():
    # Docstring
    """実行中のPythonが2系か3系かを判定する
    この関数はPython 1.xでの実行は想定していない
    """
    major = sys.version_info.major
    micro = sys.version_info.micro
    minor = sys.version_info.minor

    if major < 3:
        
        return "Python 2.x.x"
        
    else:
        version = "Python " + str(major) + "." + str(micro) + "." + str(minor)
        return print(version)

py2_or_py3()