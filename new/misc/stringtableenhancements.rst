String Table Enhancements
~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to :file:`ra2md.csf`, the game will now load --
:file:`stringtable00.csf` through :file:`stringtable99.csf`. These string tables
will add to or replace strings that were included in previously loaded string
tables.

It is also now possible to name objects in INI code (without having to create a
string table entry) by using the :value:`NOSTR:` prefix. For example,
:tag:`UIName=NOSTR:Sonar Pulse` will be displayed as "Sonar Pulse". However, the
string (including the prefix) cannot exceed 31 characters.

.. index:: String Tables; Object names can be written directly into rulesmd.ini
  rather than adding them to the string table.

The maximum number of strings in the string table has been increased to 20000.

.. index:: String Tables; Maximum number of strings increased to 20000.

.. versionadded:: 0.1
