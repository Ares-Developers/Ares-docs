.. index:: Performance; DirectDraw and Software Emulation

=================================
DirectDraw and Software Emulation
=================================

There exists a version of :file:`ddraw.dll` that is often touted as improving
the performance of :game:`Yuri's Revenge`. This "magic" DLL forces DirectDraw
into software emulation mode, which doesn't use any hardware accelerated GPU
functionality. This means special effects that are not emulated are simply
omitted, potentially improving performance. :game:`Ares` uses software emulation
mode by default, making this DLL unnecessary. However, Windows Vista and later
come with DirectX 10 - which does not support software emulation - so
:game:`Ares` will not default to software emulation mode on those versions of
Windows (otherwise users would just get a completely black screen).

.. versionadded:: 0.1
