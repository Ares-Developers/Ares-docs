================================
Bouncing Animation Damage Issues
================================

Bouncing animations would try to deal damage even if the warhead was not set,
and dealing damage could not be turned off. Thus if an animation bounced, it had
to have a valid warhead set to not risk crashes.

:game:`Ares` added the check whether :tag:`Warhead` has been set before trying
to cause any damage.

.. versionadded:: 3.0
