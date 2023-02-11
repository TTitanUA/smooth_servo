#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from setuptools import setup
import pathlib
import sdist_upip

here = pathlib.Path(__file__).parent.resolve()


# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

# load elements of version.py
exec(open(here / 'smooth_servo' / 'version.py').read())

setup(
	name="smooth_servo",
	version=__version__,
	author="TTitanUA",
	author_email="xttitanx@gmail.com",
	description="This library provides a set of slowdowns for my servo packages.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	license="MIT",
	keywords=["micropython", "servo easing"],
	platforms="micropython",
	url="https://github.com/TTitanUA/servo_smooth",
	packages=[
		"smooth_servo",
	],
	classifiers=[
		"Intended Audience :: Developers",
		"Programming Language :: Python :: Implementation :: MicroPython",
		"License :: OSI Approved :: MIT License",
	],
	python_requires='>=3.5',
	cmdclass={'sdist': sdist_upip.sdist},
)