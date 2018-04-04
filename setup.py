# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe
import sys

sys.argv.append('py2exe')
setup(
    windows=[
        {"script":"run.py","icon_resources":[(1,"logo.ico"),]}],
    options={
        "py2exe":{"includes":["sip"],"dll_excludes":["MSVCP90.dll"],\
            "bundle_files": 3,"optimize": 2,
            }},
    data_files=[
        ("image", ["./logo.ico",])]
    )