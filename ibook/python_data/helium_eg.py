#!/usr/bin/python
# -*- coding: UTF-8 -*-

from helium import *

start_chrome('github.com')
write('helium selenium github')
press(ENTER)
# click('mherrmann/helium')
go_to('github.com/login')
write('username', into='Username')
write('password', into='Password')
click('Sign in')
kill_browser()
