#!/usr/bin/env python

"""Tests for `lonlat` package."""

import unittest

from lonlat import __version__


class Testlonlat(unittest.TestCase):
    """Tests for `lonlat` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_version(self):
        assert isinstance(__version__, str)
        # 简单检查一下是不是 x.y.z 形式
        parts = __version__.split(".")
        assert len(parts) >= 2
