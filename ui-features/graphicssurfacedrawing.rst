Graphics / Surface Drawing
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning:: This is for advanced users only!

By default, most of the game's drawing surfaces are allocated in system memory,
but two of them (frequently used destination buffers) default to GPU memory.
Techniques used by the game to draw images to the screen require the former ones
to be copied to the latter ones, and this operation is fairly expensive.
:game:`Ares` allows you to allocate those surfaces in system memory, which means
the source to destination copying is almost free.

In :file:`ares.ini` you can add the following section:


::

    [Graphics.Advanced]
    DirectX.Force= (hardware|emulation)
    Surface.$surface.Memory= (System|VRAM)
    Surface.$surface.Force3D= (true|false)


...where :tag:`$surface` is one of :tag:`Composite`, :tag:`Alternate,
:tag:`Hidden`, :tag:`Sidebar` or :tag:`Tile`.

.. note:: Enabling Force3D forces Memory into VRAM mode.

.. note:: \ :game:`Ares.ini` is not intended to be included or edited by mods,
  as this file may include various other settings in future that the end-user
  wishes to set themselves. Launch Base does not permit mods to include
  \ :file:`ares.ini`, and also provides its own interface to allow the user to
  modify the above graphical settings.

.. index:: Graphics; Graphics/Surface drawing options can be configured by the user (advanced users only).

.. versionadded:: 0.1
