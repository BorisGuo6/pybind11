# KEEP IN SYNC WITH test_holder_shared_ptr.py
# -*- coding: utf-8 -*-
from pybind11_tests import holder_unique_ptr as m


def test_make_unique_pointee():
    m.to_cout("")
    m.to_cout("")
    m.to_cout("make_unique_pointee")
    obj = m.make_unique_pointee()
    assert obj.get_int() == 213
    m.to_cout("")


def test_make_shared_pointee():
    m.to_cout("")
    m.to_cout("")
    m.to_cout("make_shared_pointee")
    obj = m.make_shared_pointee()
    assert obj.get_int() == 213
    m.to_cout("")


def test_pass_unique_pointee():
    m.to_cout("")
    m.to_cout("")
    m.to_cout("pass_unique_pointee")
    obj = m.make_unique_pointee()
    assert obj.get_int() == 213
    i = m.pass_unique_pointee(obj)
    assert i == 4213
    m.to_cout("")


def test_pass_shared_pointee():
    m.to_cout("")
    m.to_cout("")
    m.to_cout("pass_shared_pointee")
    obj = m.make_unique_pointee()
    assert obj.get_int() == 213
    i = m.pass_shared_pointee(obj)
    assert i == 5213
    m.to_cout("")
