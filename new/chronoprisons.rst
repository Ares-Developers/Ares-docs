.. index::
  Chrono Prison; Abduct units from the battlefield
  Weapons; Abduct units from the battlefield like a Chrono Prison

.. index::
  Vehicles; Turret depending on passengers
  Art; Turret depending on unit's passengers

Chrono Prisons / Abductors
~~~~~~~~~~~~~~~~~~~~~~~~~~

Originally intended for :game:`Yuri's Revenge`, with published concept art and
even appearing on the original version of the box art, the Chrono Prison was
planned as a unit which would suck units into a "containment sphere" in its
turret; the turret would grow with each unit sucked in, and if the prison were
destroyed, the units would be free again. `Original concept art on the Command
& Conquer Wiki <https://cnc.fandom.com/wiki/Chrono_prison>`_.

:game:`Ares` includes functionality which can be used to create such a unit, but
the implementation is liberal enough to use the parts for a variety of other
units.

:tagdef:`[Weapon]Abductor=boolean`
  If set to :value:`yes`, weapons with this flag will absorb the target into the
  attacker's passenger hold. Should the attacking unit be destroyed, its
  passengers will emerge. Slaves' and spawned units' owner will be changed to
  the house `Special`. If the abductor is "full" or the victim cannot be
  abducted, conventional damage is dealt. Defaults to :value:`no`.

  .. note:: Please make sure you have a passenger hold when using this. Also
    remember that :tag:`SizeLimit` defaults to 0, so if you don't set it,
    abduction of most units will be denied. As usual, :tag:`PipScale` is
    required for all transports.

  .. note:: Due to the way :tag:`Passengers` for buildings was tacked on, it is
    possible buildings with abducting weapons will not work properly. (Using
    \ :tag:`InfantryAbsorb`/:tag:`UnitAbsorb` increases your chances.) These
    malfunctions are considered out of the scope of the request and will not be
    considered bugs. The same goes for :type:`InfantryTypes`. Malfunctions on
    \ :type:`VehicleTypes` and :type:`AircraftTypes`, on the other hand, should
    be reported immediately.

:tagdef:`[Weapon]Abductor.Temporal=boolean`
  Instead of abducting target units immediately, will abduct them only after
  they have been temporally erased. When the target unit would be warped away,
  it will be placed inside the abductor unit as passenger. If abduction fails,
  the target is erased normally. Requires :tag:`Temporal=yes` to be set on
  :tag:`Warhead`. Defaults to :value:`no`.

:tagdef:`[Weapon]Abductor.Anim=animation`
  This animation will be spawned at the location a unit is abducted from.
  Defaults to :value:`none`.

:tagdef:`[Weapon]Abductor.ChangeOwner=boolean`
  Sets whether the abducted unit shall change its owner to the abductor's house.
  Units which are :tag:`ImmuneToPsionics=yes` or which gained the
  :value:`PSIONICSIMMUNE` veteran ability will not change owner. Defaults to
  :value:`no`.

:tagdef:`[Weapon]Abductor.AbductBelowPercent=float - percentage`
  Specifies the percentage of health a unit has to go below to be abducted.
  Units with more health than this percentage will not be abducted. Defaults to
  :value:`100%`.

:tagdef:`[Weapon]Abductor.MaxHealth=integer - hitpoints`
  The amount of hitpoints above which it cannot be abducted any longer. If
  :value:`0`, health is not checked. Defaults to :value:`0`.

:tagdef:`[TechnoType]ImmuneToAbduction=boolean`
  Specifies whether the unit cannot be abducted. Only the conventional damage is
  dealt. Defaults to :value:`no`.

:tagdef:`[TechnoType]PassengerTurret=boolean`
  If set to yes, this unit's turret will switch to the turret with the index
  equivalent to the number of passengers it holds. Defaults to :value:`no`.


    + 0 passengers footur.vxl
    + 1 passenger footur1.vxl
    + 5 passengers footur5.vxl


  .. note:: In order to use this, you have to use YR's multi-turret logic, that
    is, you have to specify :tag:`Turret=yes`, an appropriate
    \ :tag:`TurretCount`, and you have to use the :tag:`WeaponX` flags to
    specify weapons.

.. versionadded:: 0.2
