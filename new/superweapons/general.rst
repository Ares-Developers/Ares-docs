.. index:: single: Super Weapons; Area of effect, affected houses and types, ...

General properties
``````````````````

:tagdef:`[SuperWeapon]SW.Range=float,integer`
  Most superweapons having a ranged effect can take a float or two integers. One
  float is taken as radius around the target cell, two integers separated by
  comma denote a rectangular area. For example, :tag:`SW.Range=3.5` defines a
  circle with 7 cells diameter, :tag:`SW.Range=4,6` defines a rectangle 4 cells
  wide and 6 cells high. The range is no longer bound to cell spread's
  limitation of a maximum range of 10.
:tagdef:`[SuperWeapon]SW.CreateRadarEvent=boolean`
  Creates a radar event rectangle for every player centered above the super
  weapon's target cell.
:tagdef:`[SuperWeapon]SW.AffectsHouse=enumeration none|owner|allies|team|enemies|all`
  Which houses items are affected by this super weapon. You can combine multiple
  values by comma. :value:`team` equals :value:`owner,allies`, :value:`all`
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
:tagdef:`[SuperWeapon]SW.ShowCameo=boolean`
  Sets whether this super weapon will appear in the side bar. This setting is
  ignored if :tag:`SW.AutoFire=no` is set. Defaults to :value:`yes`.
:tagdef:`[SuperWeapon]SW.Deferment=integer - frames`
  The number of frames after the fired super weapon takes effect. Not all super
  weapons support deferment.
:tagdef:`[SuperWeapon]SW.TimerVisibility=enumeration none|owner|allies|team|enemies|all`
  Defines who can see the super weapon timer, if :tag:`ShowTimer=yes`. Observers
  are considered to be allied to all players. Defaults to :value:`all`.
:tagdef:`[SuperWeapon]SW.Group=integer`
  Distinguish multiple super weapons of the same type. Defaults to :value:`0`.

.. versionadded:: 0.1
