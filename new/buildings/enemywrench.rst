.. index:: Buildings; Repair wrench not visible for enemies

Enemy Wrench
~~~~~~~~~~~~

There's a tag called :tag:`[General]EnemyHealth` to hide a unit's health bar
from enemy players. :game:`Ares` adds a new tag that does the same for the
wrench animation appearing when a player click repairs a structure.

:tagdef:`[General]EnemyWrench=boolean`
  Whether players not allied with the owning player can see the repair wrench
  animation playing if the building is click repaired. Observers can always see
  the wrench animation. Defaults to :value:`yes`.

  .. note:: The wrench animation will not show if a building is being attacked
    by a temporal weapon or an enemy building is cloaked.

.. versionadded:: 0.8
