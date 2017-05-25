Saboteurs
~~~~~~~~~

:game:`Dune 2000` had the Saboteur, an infantry unit that could enter enemy
structures and destroy them immediately, sacrificing himself. This has been
re-created in :game:`Ares`.

Only buildings owned by enemy players are sabotagable. If a building can be
sabotaged, the player gets the cursor named :value:`Sabotage`, which is a new
customizable :doc:`Mouse Cursor </new/mousecursors>`.

.. note:: The temporary cloak feature has not been implemented.

:tagdef:`[InfantryType]Saboteur=boolean`
  Whether this infantry can blow up a sabotagable building. The building will be
  destroyed as if C4 was placed, and the Saboteur is consumed in this process.
  Requires :tag:`Infiltrate=yes`. Not supported together with vehicle hijacking,
  :tag:`CanDrive=yes`, C4 (either :tag:`C4=yes` or granted through veterancy)
  and :tag:`Occupier=yes` logics. Defaults to :value:`no`.

:tagdef:`[BuildingType]ImmuneToSaboteurs=boolean`
  Whether this building cannot be sabotaged. If :value:`yes`, saboteurs cannot
  enter this structure. Defaults to :value:`yes` for :tag:`CanC4=no` or
  :tag:`TechLevel=-1` :tag:`CanBeOccupied=yes` buildings, to :value:`no`
  otherwise.

  .. note: By default, unbuildable occupiable structures cannot be sabotaged.
    This prevents saboteurs from blowing up civilian structures when selected in
    a group with occupiers. This default value might change in the future.

.. index:: InfantryTypes; Saboteurs blowing up buildings

.. versionadded:: 0.A
