.. index:: Tech Structures; NeedsEngineer is honored when playing animations.

==============================
Tech Structures and Animations
==============================

:tag:`NeedsEngineer` controls whether a tech building is offline until it is
captured by an engineer. Until then, it should not play any active animations,
yet when a building with :tag:`NeedsEngineer=yes` was damaged into yellow health
and switched to the damaged graphics, the animations started to play as if it
had been captured. This did not affect the functionality, though. With
:game:`Ares` the animations will not start to play in this case.

.. versionadded:: 0.6
