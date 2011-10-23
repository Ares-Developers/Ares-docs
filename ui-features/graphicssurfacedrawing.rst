Graphics / Surface Drawing
~~~~~~~~~~~~~~~~~~~~~~~~~~

*This is for advanced users only!* By default, most of the game's
drawing surfaces are allocated in system memory, but two of them
(frequently used destination buffers) default to GPU memory.
Techniques used by the game to draw images to the screen require the
former ones to be copied to the latter ones, and this operation is
fairly expensive. Ares allows you to allocate those surfaces in system
memory, which means the source to destination copying is almost free.

In ares.ini you can add the following section:


::

    [Graphics.Advanced]
    		DirectX.Force= (hardware|emulation)
    		Surface.$surface.Memory= (System|VRAM)
    		Surface.$surface.Force3D= (true|false)


...where $surface is one of Composite, Alternate, Hidden, Sidebar or
Tile.

NB: enabling Force3D forces Memory into VRAM mode.
NB: Ares.ini is not intended to be included or edited by mods, as this
file may include various other settings in future that the end-user
wishes to set themselves. Launch Base does not permit mods to include
ares.ini, and also provides its own interface to allow the user to
modify the above graphical settings. Graphics/Surface drawing options
can be configured by the user (advanced users only).

.. versionadded:: 0.1










