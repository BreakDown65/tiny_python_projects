#!/usr/bin/env python3
"""tests for hello.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = 'hello.py'
run = f'python {prg}'


def test_exists():
    assert os.path.isfile(prg)


def test_runnable():
    out = getoutput(run)
    assert out.strip() == 'Hello, World!'


def test_executable():
    out = getoutput(run)
    assert out.strip() == 'Hello, World!'


def test_usage():
    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{run} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


def test_input():
    for val in ['Universe', 'Multiverse']:
        for option in ['-n', '--name']:
            rv, out = getstatusoutput(f'{run} {option} {val}')
            assert rv == 0
            assert out.strip() == f'Hello, {val}!'