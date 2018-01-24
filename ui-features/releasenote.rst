.. index:: Mods; Release note printed on-screen

Release Note
~~~~~~~~~~~~

If your mod is still in early development stage or in testing phase, you can
make :game:`Ares` display a release note in the lower left corner of the screen.
The text can contain the current version, warnings or other details. It will
appear in-game as red text on black background.

The release note is the text in the CSF files labeled :value:`TXT_RELEASE_NOTE`.
Include a string with this label in a stringtable file (not in
:file:`ra2md.csf`) to enable the text.

.. note:: \ :game:`Ares` includes an empty text for this label to ensure the
  string can be found and "MISSING:TXT_RELEASE_TEXT" is not displayed on the
  screen.

.. versionadded:: 0.4
