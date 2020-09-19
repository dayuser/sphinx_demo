#!/usr/bin/python
# -*- coding: UTF-8 -*-

from pywinauto.application import Application
app = Application().start("notepad.exe")

app.UntitledNotepad.menu_select("帮助->关于记事本")

app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)

