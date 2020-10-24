.. index:: single: Super Weapons; Area of effect, affected houses and types, ...

General Settings
````````````````

.. versionadded:: 0.1


Common Settings
---------------

:tagdef:`[SuperWeapon]SW.Range=float,integer`
  Most superweapons having a ranged effect can take a float or two integers. One
  float is taken as radius around the target cell, two integers separated by
  comma denote a rectangular area. For example, :tag:`SW.Range=3.5` defines a
  circle with 7 cells diameter, :tag:`SW.Range=4,6` defines a rectangle 4 cells
  wide and 6 cells high. The range is no longer bound to cell spread's
  limitation of a maximum range of 10.
:tagdef:`[SuperWeapon]SW.Deferment=integer - frames`
  The number of frames after the fired super weapon takes effect. Not all super
  weapons support deferment.
:tagdef:`[SuperWeapon]SW.CreateRadarEvent=boolean`
  Creates a radar event rectangle for every player centered above the super
  weapon's target cell.
:tagdef:`[SuperWeapon]SW.ShowCameo=boolean`
  Sets whether this super weapon will appear in the side bar. This setting is
  ignored if :tag:`SW.AutoFire=no` is set. Defaults to :value:`yes`.
:tagdef:`[SuperWeapon]SW.TimerVisibility=enumeration none|owner|allies|team|enemies|all`
  Defines who can see the super weapon timer, if :tag:`ShowTimer=yes`. Observers
  are considered to be allied to all players. Defaults to :value:`all`.
:tagdef:`[SuperWeapon]SW.Group=integer`
  Distinguish multiple super weapons of the same type. Defaults to :value:`0`.


Affected Targets
----------------

:tagdef:`[SuperWeapon]SW.AffectsHouse=enumeration none|owner|allies|team|enemies|all`
  Which houses items are affected by this super weapon. You can combine multiple
  values by comma. :value:`team` equals :value:`owner,allies`, and :value:`all`
  equals :value:`owner,allies,enemies`. Defaults to :value:`team` for the Force
  Shield, to :value:`all` otherwise.
:tagdef:`[SuperWeapon]SW.AffectsTarget=enumeration none|land|water|empty|infantry|units|buildings`
  Which items are allowed to be affected by this super weapon. You can combine
  multiple values by comma. If you don't specify either land or water, both will
  be allowed. If you don't specify any of the other values, everything can be
  affected. Thus, if you specify no restriction (:value:`none`), all targets are
  valid. For example, :tag:`SW.AffectsTarget=land,buildings` affects all
  buildings that aren't water-bound, :tag:`SW.AffectsTarget=water` affects every
  water cell, occupied or empty.


Charging Settings
-----------------

:tagdef:`[SuperWeapon]SW.InitialReady=boolean`
  Whether the first super weapon of this type will be ready to fire immediately
  after the super weapon becomes available. Once the super weapon has been
  fired once, it will recharge normally. Defaults to :value:`no`.
:tagdef:`[SuperWeapon]SW.VirtualCharge=boolean`
  Once the super weapon becomes available, it will charge continuously, even if
  the the owning player loses all buildings that provide it. The super weapon
  will continue to charge in the background or outside the map. When the cameo
  is removed and added again, the super weapon will appear with the cameo charge
  already partially progressed instead of restarting to charge. Defaults to
  :value:`no`.

  .. note:: Virtual charge is not supported on :tag:`UseChargeDrain=yes` super
    weapons.

.. versionadded:: 3.0
