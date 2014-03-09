"""
Test for basic math operations
"""

from . import TestCase

class TestLoadExtraPlugins(TestCase):
    from bitmath import *

    def setUp(self):
        self.num1 = KiB(3)
        self.num2 = KiB(1337)

    def test_add(self):



    # def test_load_extra_plugins(self):
    #     """
    #     Verify that we can load plugins from user-defined locations
    #     """
    #     loaded = load_extra_plugins(self._extra_dir)
    #     total_loaded = len(loaded)
    #     self.assertEqual(total_loaded, 1, msg="Loaded %d plugins (%s), expected 1" % (total_loaded, ', '.join(loaded)))

    # def test_load_compound_path(self):
    #     """
    #     Verify that we can load plugins from a compound pathspec
    #     """
    #     compound_pathspec = "%s:%s" % self._extra_plugin_dirs
    #     loaded = load_extra_plugins(compound_pathspec)
    #     total_loaded = len(loaded)
    #     self.assertEqual(total_loaded, 2, msg="Loaded %d plugins (%s), expected 2" % (total_loaded, ', '.join(loaded)))

    # def tearDown(self):
    #     # Cleanup all of our temporary files
    #     for d in self._extra_plugin_dirs:
    #         for f in self.os.listdir(d):
    #             ff = self.os.path.join(d, f)
    #             self.os.remove(ff)
    #         self.os.rmdir(d)
