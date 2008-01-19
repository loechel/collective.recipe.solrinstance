# -*- coding: utf-8 -*-
"""Recipe solrinstance"""

class Recipe(object):
    """This recipe is used by zc.buildout"""

    def __init__(self, buildout, name, options):
        self.name, self.options = name, options

    def install(self):
        """installer"""
        # XXX do the job here
        # returns installed files
        return tuple()

    def update(self):
        """updater"""
        pass
