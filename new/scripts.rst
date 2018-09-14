Script Actions
~~~~~~~~~~~~~~

:captiontag:`Gather at Enemy` (53)
``````````````````````````````````

The previously unused parameter of the :value:`Gather at Enemy` script action is
now added to :tag:`[General]AISafeDistance` to determine the distance from the
center of the enemy base the team should gather at. Can be negative to shorten
the distance.

.. versionadded:: 2.0



.. index:: Scripts; Distance setting for Gather at Base

:captiontag:`Gather at Base` (54)
`````````````````````````````````

:game:`Ares` splits the tag :tag:`[General]AISafeDistance` into two, which is
used for two similar team script actions serving different purposes.

:tagdef:`[General]AIFriendlyDistance=integer - cells`
  Cell distance the AI will use for gathering outside the owning player's base
  using script action 54. Defaults to :tag:`[General]AISafeDistance`.

Like for the :value:`Gather at Enemy` script action, the previously unused
parameter of the :value:`Gather at Base` script action is now added to the
distance from the center of the own base the team should gather at. Can be
negative to shorten the distance.

.. versionadded:: 2.0



.. _script-ironcurtain:

.. index:: Scripts; Iron Curtain team script extended

:captiontag:`Iron Curtain` (55)
```````````````````````````````

Previously, the game would only look at the first (and usually only) super
weapon with :tag:`Type=IronCurtain`, then check whether it was either ready or
almost charged. If that was not the case, the script action failed.

:game:`Ares` will instead check all super weapon with
:tag:`SW.AITargetingMode=IronCurtain` and will fire the first one that is fully
charged, or wait, if any is at least almost charged. The script will fail
otherwise.

The previously unused parameter of the :value:`IronCurtain` script action is now
used to denote the group the Iron Curtain super weapon has to belong to before
being considered. This allows to create super weapon groups (for instance for
traditional Iron Curtain and new AttachEffect boosts) and different teams to
rely on different super weapon groups.

.. versionadded:: 2.0
