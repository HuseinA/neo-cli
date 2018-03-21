"""Tests for our `neo hello` subcommand."""

from subprocess import PIPE, Popen as popen
from unittest import TestCase
from neo.libs import login


class TestHello(TestCase):
    def test_login(self):
        output = login.do_login()
        self.assertTrue(output)
