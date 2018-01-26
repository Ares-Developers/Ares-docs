.. index:: Sounds; Multiple custom audio.bag files

Additional Bag Files
~~~~~~~~~~~~~~~~~~~~

:game:`Yuri's Revenge` only read :file:`audio.idx` and :file:`audio.bag`, either
requiring modders to deliver custom versions also including the original sound
files, or to rely on loose wave files.

:game:`Ares` adds support for multiple index and bag files, which make it easier
to deliver sounds while also decreasing the mod's file sizes potentially. First
:file:`audio.idx` is read as before, and then all files from :file:`audio01.idx`
to :file:`audio99.idx`, with the actual data in the corresponding :file:`.bag`
file.

Index files loaded later can override sound files that were included earlier,
thus it is possible to update sound files using relatively small bag files for
patches.

.. versionadded:: 0.A
