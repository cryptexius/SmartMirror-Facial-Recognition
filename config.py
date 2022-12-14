#!/usr/bin/python
# coding: utf8

import os
import json
import sys
import platform

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/common/'))
sys.path.insert(0, "/home/cryptexius/Projects");

from commonconfig import CommonConfig
from huskylib import HuskyLensLibrary


class MMConfig (CommonConfig):
    
    CONFIG_DATA = json.loads(sys.argv[1]);
    INTERVAL_ATTR = 'interval'
    LOGOUT_DELAY_ATTR = 'logoutDelay'
    USERS_ATTR = 'users'
    DEFAULT_CLASS_ATTR = 'defaultClass'
    EVERYONE_CLASS_ATTR = 'everyoneClass'
    WELCOME_MESSAGE_ATTR = 'welcomeMessage'
    
    @classmethod
    def toNode(cls, type, message):
        print(json.dumps({type: message}))
        sys.stdout.flush()
    @classmethod
    def getInterval(cls):
        return cls.get(cls.INTERVAL_ATTR)
    @classmethod
    def getLogoutDelay(cls):
        return cls.get(cls.LOGOUT_DELAY_ATTR)
    @classmethod
    def getUsers(cls):
        return cls.get(cls.USERS_ATTR)
    @classmethod
    def getDefaultClass(cls):
        return cls.get(cls.DEFAULT_CLASS_ATTR)
    @classmethod
    def getEveryoneClass(cls):
        return cls.get(cls.EVERYONE_CLASS_ATTR)
    @classmethod
    def getWelcomeMessage(cls):
        return cls.get(cls.WELCOME_MESSAGE_ATTR)
    
    @classmethod
    def get(cls, key):
        return cls.CONFIG_DATA[key]