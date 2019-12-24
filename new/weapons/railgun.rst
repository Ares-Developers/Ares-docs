.. index:: Weapons; Detached railgun beams

Detached Railgun Beams
``````````````````````

A unit cannot fire another railgun beam as long as the previously fired beam
dissolved completely. This new setting allows to get around that limitation.

.. warning:: Mind that this could mean creating a large amount of particles, so
  overusing this feature might cause lag.

:tagdef:`[Weapon]IsDetachedRailgun=boolean`
  Whether this weapon is a railgun. Has the same particle effect as
  :tag:`IsRailgun` but does not have the limitation that the weapon cannot be
  fired again as long as the particle system created by firing the weapon
  previously subsided. Defaults to :value:`no`.

  .. note:: Combining :tag:`IsDetachedRailgun=yes` with :tag:`IsRailgun=yes` is
    not supported.

.. versionadded:: 3.0
