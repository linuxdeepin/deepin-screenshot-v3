#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2014 ~ 2015 Deepin, Inc.
#               2014 ~ 2015 Wang Yaohua
#
# Author:     Wang Yaohua <mr.asianwang@gmail.com>
# Maintainer: Wang Yaohua <mr.asianwang@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from sina_weibo import SinaWeibo

class AccountsManager(object):
    """Manager of all the SNS accounts"""
    def __init__(self):
        super(AccountsManager, self).__init__()
        self._sina_weibo = SinaWeibo()

    def setWeiboAccount(self, uid):
        self._sina_weibo.setUID(uid)

    def share(self, text, pics=None):
        self._sina_weibo.enabled = True
        self._sina_weibo.share(text, pics)