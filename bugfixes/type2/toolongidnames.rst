.. index:: Debugging; Warning if a too long ID is used

==================================
Warning When a Too Long ID is Used
==================================

If the game tries to instantiate a type with an ID longer than 24 characters,
:game:`Ares` will show a dialog pointing out the ID used. This happens if a type
list includes a too long ID directly, or for example, if the game automatically
adds a too long type ID it encountered to the list while parsing an INI section.
This always indicates a bug, and this always is a bug present in a modded INI
or map file.

.. note:: This feature does not catch too long IDs present in INI sections that
  are not automatically added to the type list while parsing. Searching for the
  exact ID will just fail. Only if the tag is read by :game:`Ares`, a warning
  will be emitted in the debug log.

.. versionadded:: 3.0
