.. index:: Theaters; Alternate Theater Art for all BuildingTypes regardless of first letter.

===============================================
Alternate Theater Art For :type:`BuildingTypes`
===============================================

:type:`BuildingTypes` whose :file:`artmd.ini` entry has :tag:`NewTheater=yes`
set would have the second letter of their SHP filenames replaced by another
letter, depending on the theater of the current map. For example,
:tag:`[GAWEAP]` uses SHP files named :file:`GAWEAP*` on arctic maps,
:file:`GTWEAP*` on temperate maps, :file:`GDWEAP*` on desert maps and so on. In
the event that a SHP file with the appropriate filename does not exist, the game
falls back to :file:`GGWEAP*`.

However, in :game:`Yuri's Revenge` this filename-adjusting logic only works for
:type:`BuildingTypes` whose :tag:`Image` ID starts with G, N, Y or C.
:game:`Ares` extends this logic to work for :tag:`Image` IDs starting with any
letter (A-Z or a-z).

.. versionadded:: 0.2
