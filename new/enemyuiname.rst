:captiontag:`EnemyUIName`
~~~~~~~~~~~~~~~~~~~~~~~~~

In :game:`Yuri's Revenge`, allies and enemies alike can see the name of any unit
and structure. In the earlier games, the tooltip would for example show "Enemy
Structure" instead. This setting is useful to hide the name of fake structures.

:tagdef:`[BuildingType]EnemyUIName=csf string`
  Optional name used for enemy buildings. Observers, allies, and players who
  infiltrated the building will see the real name defined by :tag:`UIName`, all
  other players will see this name.

  .. note:: This tag is currently limited to :type:`BuildingTypes`. It might be
    expanded to other :type:`TechnoTypes` in the future.

.. index:: Technos; Hide the actual name from enemies

.. versionadded:: 0.B
