.. Ares documentation master file, created by
   sphinx-quickstart on Sun Oct 23 13:14:19 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

==================
Ares Documentation
==================

Introduction
============
:game:`Ares` is the new tool to extend the capabilities of :game:`Yuri's
Revenge`. It was conceived by pd near the end of 2007, and is currently in an
early development and testing cycle.

This documentation is aimed primarily at :game:`Ares` testers, as :game:`Ares`
is a work in progress and subject to many further changes. However, the
documentation is also aimed at mod authors wishing to make use of the new
functionality that :game:`Ares` offers.

:game:`Ares` is incorporated into :game:`Yuri's Revenge` via the use of
:game:`Syringe`, a program developed by pd to 'inject' DLL code into a running
executable without modifying the executable itself. In this case, the
:game:`Ares` DLL is injected into the :game:`Yuri's Revenge` 1.001 main
executable, :file:`gamemd.exe`.

:game:`Syringe` can be run directly via a command line prompt, or automatically
using :game:`Launch Base`. See the respective documentations of those programs
for further details.


Table of Contents
=================

.. toctree::
	:maxdepth: 1
	
	notes
	whatsnew
	migration

.. toctree::
	:maxdepth: 2
	
	bugfixes/index

.. toctree::
	:maxdepth: 3
	
	restored/index
	new/index
	ui-features/index
	
	comparison
	credits
	glossary

* :ref:`Overview of Ares's Bugfixes and Features <genindex>`
* :ref:`search`
