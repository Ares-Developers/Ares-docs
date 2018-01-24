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
Revenge` and to fix bugs in the game engine. It was conceived by pd near the end
of 2007, developed over the years by :doc:`The Ares Contributors </credits>` and
first released to the public in 2010.

This documentation is aimed primarily at mod authors wishing to make use of the
new functionality that :game:`Ares` offers.

:game:`Ares` is incorporated into :game:`Yuri's Revenge` via the use of
:game:`Syringe`, a program initially developed by pd to 'inject' DLL code into a
running executable without modifying the executable file itself.

In this case, the :game:`Ares` DLL is injected into the :game:`Yuri's Revenge`
1.001 main executable, :file:`gamemd.exe`. The properly patched original CD
version as well as the compilations :game:`The First Decade` and :game:`The
Ultimate Collection` are supported.

:game:`Syringe` can be run directly via a command line prompt or automatically
run from external launcher applications provided by a mod. See the respective
documentations of those programs for further details.


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
