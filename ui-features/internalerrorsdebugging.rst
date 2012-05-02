Internal Errors / Debugging
~~~~~~~~~~~~~~~~~~~~~~~~~~~

When an Internal Error occurs, the :file:`except.txt` file that is produced has
been modified so as to output more information that is both relevant to mod
authors, and also relevant to us, the developers, when debugging the changes and
additions introduced by :game:`Ares`.

:file:`except.txt` may include a timestamp in the filename to prevent an
existing :file:`except.txt` file being overwritten.

:game:`Ares` will give you the option to produce a crash dump file to assist in
determining the cause of the error. This file will be stored in a Debug folder
within the main game directory. Note that the crash dump file is very large and
may only be readable by the :game:`Ares` developers. Like :file:`except.txt`,
this file will include a timestamp in the filename.

If you have turned on debug logging (see :doc:`Command Line Arguments
</ui-features/commandlinearguments>` and :ref:`Debug Logging <debug-logging>`)
then the game will produce a :file:`debug.log` file in the aforementioned Debug
folder. Like :file:`except.txt`, this file will include a timestamp in the
filename. The log file may contain useful information for helping diagnose
problems with your mod or :game:`Ares` itself.

In the event of an Internal Error, :game:`Ares` can sometimes tell you what
caused the error. For example:


Here, :game:`Ares` can determine what caused the error.


Here, the error cannot be figured out - :game:`Ares` offers to create a full
crash report.


The crash report has been generated. :game:`Ares` will close after showing this
message.

Some potential errors may now be triggered when loading rather than waiting for
the error to crop up in game. Critical errors occur always, less critical errors
occur only if you have used the :doc:`-STRICT command line argument
</ui-features/commandlinearguments>`.

.. index:: Improved Internal Error handling and debug logs to assist with debugging mods/Ares.

.. versionadded:: 0.1
