Animations and :captiontag:`Rotates=yes`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Projectiles with :tag:`Rotates=yes` used their image's 32 frames to represent
moving in differnent directions, one frame per facing. This means these
projectiles did not support being animated. :game:`Ares` adds support for this.

:tagdef:`[Projectile]AnimLength=integer - frames`
  The number of frames the animation for each facing has. Playback speed is one
  frame every :tag:`AnimRate` frames. The animation is not guaranteed to play
  from the first frame on. Defaults to :value:`1`.

  .. note:: \ :tag:`AnimRate` cannot be :value:`0`, or a division by zero will
    crash the game once a projectile of this type is fired.

.. versionadded:: 0.9
