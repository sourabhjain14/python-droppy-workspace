#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import py
import pytest
import shutil
import task

files_dir = py.path.local(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'Test', 'files'))


def test_input_empty(tmpdir):
    input_dir = tmpdir.join('0')
    os.makedirs('%s' % input_dir)

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    t = task.Task(input_dir='%s' % input_dir,
                  output_dir='%s' % output_dir)

    assert isinstance(t, object)


def test_external_executable_na(tmpdir):
    input_dir = tmpdir.join('0')
    os.makedirs('%s' % input_dir)

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    with pytest.raises(SystemExit) as exc_info:
        t = task.Task(input_dir='%s' % input_dir,
                      output_dir='%s' % output_dir,
                      ebookconvert_executable='/this/path/does/not/exist')

    assert exc_info.type == SystemExit


def test_input_file(tmpdir):
    input_dir = tmpdir.join('0')
    os.makedirs('%s' % input_dir)

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    shutil.copyfile('%s' % files_dir.join('pg5903.epub'),
                    '%s' % input_dir.join('pg5903.epub'))

    t = task.Task(input_dir='%s' % input_dir,
                  output_dir='%s' % output_dir)

    assert output_dir.join('pg5903.mobi').check() is True


def test_input_folder(tmpdir):
    input_dir = tmpdir.join('0')
    os.makedirs('%s' % input_dir)

    content_dir = input_dir.join('content')
    os.makedirs('%s' % content_dir)

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    shutil.copyfile('%s' % files_dir.join('pg5903.epub'),
                    '%s' % content_dir.join('pg5903.epub'))

    t = task.Task(input_dir='%s' % input_dir,
                  output_dir='%s' % output_dir)

    assert output_dir.join('content', 'pg5903.mobi').check() is True
