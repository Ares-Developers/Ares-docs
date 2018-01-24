.. index::
  Disk Lasers; Animations and Bright
  Weapons; Disk Lasers with animations and Bright

Disk Laser Animations
~~~~~~~~~~~~~~~~~~~~~

Even though pre-release screen shots showed this, :tag:`DiskLaser=yes` weapons
do not display animations from their warheads :tag:`AnimList`. :game:`Ares`
automatically respects the :tag:`Bright` setting on the weapon and adds a way to
enable animations.

This global tag has to be enabled manually so the game's default is not changed,
because the Disk Laser weapons in :game:`Yuri's Revenge` have animations set.

:tagdef:`[AudioVisual]DiskLaserAnimEnabled=boolean`
  Whether Disk Lasers should display an animation from their warhead's
  :tag:`AnimList`. Defaults to :value:`no`.

.. versionadded:: 0.A
