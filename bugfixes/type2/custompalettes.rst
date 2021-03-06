.. index:: Palettes; Units can specify a custom palette.

===============
Custom Palettes
===============

The original game supports custom palettes on TechnoTypes using
``Palette`` (filename, excluding .pal extension) on the TechnoType's
entry in :file:`artmd.ini`. However, the game would crash (with the message
"You have violated the limit of having only one extra building
Palette" in the (non-existent) log file) if you used the ``Palette``
flag more than once. And, of course, the one extra palette was already
in use on the Statue of Liberty. Ares removes this limit and lets you
use custom palettes on all TechnoTypes to your heart's content.

.. note:: It is not known why this apparently arbitrary limit on custom
	palettes was in place it may have been there to mask a bug that we
	don't yet know about.

.. note:: When using custom palettes, the modder must make a new palette for
	each theater. Normally, each building or unit has an associated
	palette for each theater it can be deployed into (EG "unitsno.pal",
	"unittem.pal", etc). If the modder creates a new palette, say
	"picasso.pal", in order for that palette to be used in other theatres,
	the modder must create "picassosno.pal", "picassotem.pal", etcetera as
	well.

.. versionadded:: 0.1
