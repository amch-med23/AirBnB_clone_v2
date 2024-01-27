#!/usr/bin/python3
""
import unittest
from unittest import mock
from io import StringIO
from os import remove
from console import HBNBCommand


class Test_console(unittest.TestCase):
    """"""

    def tearDown(self):
        remove('file.json')

    @staticmethod
    def run_command(command):
        """ runs commands using the console and returns the output """
        stdout = StringIO()

        with mock.patch('sys.stdout', stdout):
            cli = HBNBCommand()
            cli.onecmd(command)
        return stdout.getvalue()

    def test_do_create(self):
        """"""
        output = self.run_command('create City')
        self.assertEqual(len(output.strip()), 36)

    def test_do_all_empty(self):
        output = self.run_command('all')
        print(output)
        self.assertEqual(output, '[]')
