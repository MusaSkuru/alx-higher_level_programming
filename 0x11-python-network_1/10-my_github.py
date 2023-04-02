#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 07:02:53 2023
@author: Musa Skuru
"""
from requests import get
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
        url = 'https://api.github.com/user'
            username = argv[1]
                password = argv[2]
                    response = get(url, auth=HTTPBasicAuth(username, password))
                        try:
                                    obj = response.json()
                                            print(obj.get('id'))
                                                except ValueError:
                                        
