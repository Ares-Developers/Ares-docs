String Table Enhancements
~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to ra2md.csf, the game will now load stringtable00.csf
through stringtable99.csf. These string tables will add to or replace
strings that were included in previously loaded string tables.

It is also now possible to name objects in INI code (without having to
create a string table entry) by using the `NOSTR:` prefix. For
example, `UIName=NOSTR:Sonar Pulse` will be displayed as " *Sonar
Pulse*". However, the string (including the prefix) cannot exceed 31
characters. Object names can be written directly into rulesmd.ini
rather than adding them to the string table.

.. versionadded:: 0.1



<<<SEPARATOR>>>
