.. index:: Palettes; Units can specify a custom palette.

===============
Custom Palettes
===============

The original game supports custom palettes on :type:`TechnoTypes` using
:tag:`Palette` (filename, excluding .pal extension) on the :type:`TechnoType`'s
entry in :file:`artmd.ini`. However, the game would crash (with the message "You
have violated the limit of having only one extra building Palette" in the
[non-existent] log file) if you used the :tag:`Palette` flag more than once.
And, of course, the one extra palette was already in use on the Statue of
Liberty. :game:`Ares` removes this limit and lets you use custom palettes on all
:type:`TechnoTypes` to your heart's content.

See :doc:`/new/customanimationandprojectilepalettes`.

.. note:: It is not known why this apparently arbitrary limit on custom palettes
  was in place it may have been there to mask a bug that we don't yet know
  about.

.. note:: When using custom palettes, the modder must make a new palette for
  each theater. Normally, each building or unit has an associated palette for
  each theater it can be deployed into (e.g. :file:`unitsno.pal`,
  \ :file:`unittem.pal`, etc). If the modder creates a new palette, say
  "picasso.pal", in order for that palette to be used in other theatres, the
  modder must create "picassosno.pal", "picassotem.pal", etc as well.

.. versionadded:: 0.1
