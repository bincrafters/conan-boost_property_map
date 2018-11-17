#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostProperty_MapConan(base.BoostBaseConan):
    name = "boost_property_map"
    url = "https://github.com/bincrafters/conan-boost_property_map"
    lib_short_names = ["property_map"]
    header_only_libs = ["property_map"]
    cycle_group = "boost_level14group"
    b2_requires = [
        "boost_level14group",
    ]


