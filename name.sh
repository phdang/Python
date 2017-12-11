#!/usr/bin/env python
import os
program = raw_input('New respository name: ')
url1= """curl -u phdang https://api.github.com/user/repos -d '{ "name": """
url2='"'
url3= """ }'"""
url=url1+url2+program+url2+url3
os.system(url)
