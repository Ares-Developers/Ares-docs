.. index::
  Tiberium; Units can heal on tiberium
  Universe; Tiberium heals units

Tiberium Heal
`````````````

Tiberium Heal is the effect of units gaining hitpoints when standing or moving
over cells containing tiberium. This feature from :game:`Tiberian Sun` has been
restored and made more customizable.

.. versionadded:: 0.5


Enabling Tiberium Heal
----------------------

:game:`Ares` requires a new tag to be set to enable the Heal feature, and it
does no longer heal units that are positioned above :tag:`[General]HoverHeight`.

:tagdef:`[General]TiberiumHealEnabled=boolean`
  Whether tiberium is allowed to heal units. Required for the following tags to
  work. Defaults to :value:`no`.

:tagdef:`[General]TiberiumHeal=float - minutes`
  The interval between healing steps being applied in minutes. Defaults to
  :value:`1.13333` (once each 68 seconds).


Who will heal
-------------

Enabling the Tiberium Heal feature depending on the unit type can be done by
setting a tag or by granting the :value:`TIBERIUM_HEAL` veteran ability like in
:game:`Tiberian Sun`.

:tagdef:`[TechnoType]TiberiumHeal=boolean`
  Whether this unit heals if standing on a cell containing Tiberium. Defaults to
  :value:`no`.

  .. note:: If :value:`yes`, units leave behind a random amount of tiberium when
    destroyed or killed by default. This can be customized. See :ref:`Tiberium
    Remains <tiberium-remains>`.


How much how often
------------------

The delay between the effect being applied and amount of hitpoints to be
restored can be customized for each unit type and for each of the
:type:`Tiberiums`. The default tags are also used for other repair logics, so
the following tags can be used to balance the Tiberium Heal independently from
them.

.. note Note that :game:`Tiberian Sun` did not make a distinction between
  \ :type:`VehicleTypes` and :type:`AircraftTypes`. It applied
  \ :tag:`[General]RepairStep` to both.

:tagdef:`[Tiberium]Heal.Delay=float - minutes`
  The interval between healing steps being applied in minutes. Defaults to
  :tag:`[General]TiberiumHeal`.

:tagdef:`[Tiberium]Heal.Step=integer`
  The health to restore for :type:`AircraftTypes` after each delay. Defaults to
  :tag:`[General]RepairStep`.

:tagdef:`[Tiberium]Heal.IStep=integer`
  The health to restore for :type:`InfantryTypes` after each delay. Defaults to
  :tag:`[General]IRepairStep`.

:tagdef:`[Tiberium]Heal.UStep=integer`
  The health to restore for :type:`VehicleTypes` after each delay. Defaults to
  :tag:`[General]URepairStep`.


.. _tiberium-remains:

.. index:: Tiberium; Units leave behind tiberium when destroyed

Tiberium Remains
````````````````

In :tag:`Tiberian Sun` units that had :tag:`TiberiumHeal=yes` (not the
:value:`TIBERIUM_HEAL` veteran ability) left behind a random amount of tiberium
when destroyed or killed. This hardcoded behavior is now customizable and
working independently of Tiberium Heal.

Up to five bails are left behind in the adjacent cells, depending on whether the
tiberium can be added to them.

:tagdef:`[TechnoType]TiberiumRemains=boolean`
  Whether this unit leaves behind tiberium when destroyed. Defaults to
  :tag:`TiberiumHeal` if :tag:`[General]TiberiumHealEnabled=yes`, to :value:`no`
  otherwise.

.. versionadded:: 0.5
