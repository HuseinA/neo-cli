"""Tests for our `neo hello` subcommand."""

from subprocess import PIPE, Popen as popen
from unittest import TestCase


class TestHello(TestCase):
    def test_returns_multiple_lines(self):
        output = popen(['neo', 'login'], stdout=PIPE).communicate()[0]
        lines = output.split('\n')
        self.assertTrue(len(lines) != 1)