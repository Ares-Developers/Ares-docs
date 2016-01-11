String Table Enhancements
~~~~~~~~~~~~~~~~~~~~~~~~~

More String Tables
``````````````````

In addition to :file:`ra2md.csf`, the game will now load --
:file:`stringtable00.csf` through :file:`stringtable99.csf`. These string tables
will add to or replace strings that were included in previously loaded string
tables.

.. versionadded:: 0.1


NOSTR Prefix
````````````

It is also now possible to name objects in INI code (without having to create a
string table entry) by using the :value:`NOSTR:` prefix. For example,
:tag:`UIName=NOSTR:Sonar Pulse` will be displayed as "Sonar Pulse". However, the
string (including the prefix) cannot exceed 31 characters.

.. index:: String Tables; Object names can be written directly into rulesmd.ini
  rather than adding them to the string table.

.. versionadded:: 0.1


Maximum Number of Strings
`````````````````````````

The maximum number of strings in the string table has been increased to 20000.

.. index:: String Tables; Maximum number of strings increased to 20000.

.. versionadded:: 0.2


Language-Neutral String Tables
``````````````````````````````

String tables can now be marked as 'language neutral' by setting the language
field in the header to :value:`-1` (or :value:`FF FF FF FF` in hexadecimal).
Files that are language neutral will always load, no matter what language the
main string table :file:`ra2md.csf` is.

If your string table editor does not support setting the language manually, use
a hex editor to set the four bytes starting at offset 0x14 directly.

.. index:: String Tables; Language-neutral string tables

.. versionadded:: 0.A
