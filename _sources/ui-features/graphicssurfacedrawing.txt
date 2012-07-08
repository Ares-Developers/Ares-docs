Graphics / Surface Drawing
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning:: This is for advanced users only!

In :file:`ares.ini` you can add the following section:

::

    [Graphics.Advanced]
    DirectX.Force= (hardware|emulation)

While :value:`hardware` is the default, :value:`emulation` has the same effect
as the special :file:`ddraw.dll` which made the games faster by not drawing
the effects that aren't supported by software emulation.

.. note:: \ :value:`emulation` is not available on Windows Vista and later.
  \ :game:`Ares` defaults to :value:`hardware` on such systems.

.. note:: \ :game:`Ares.ini` is not intended to be included or edited by mods,
  as this file may include various other settings in future that the end-user
  wishes to set themselves. Launch Base does not permit mods to include
  \ :file:`ares.ini`, and also provides its own interface to allow the user to
  modify the above graphical settings.

.. versionadded:: 0.1
