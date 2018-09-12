Script Actions
~~~~~~~~~~~~~~

.. _script-ironcurtain:

.. index:: Scripts; IronCurtain team script extended

:captiontag:`IronCurtain` (55)
``````````````````````````````

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
