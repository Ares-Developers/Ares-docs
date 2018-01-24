.. index:: Universe; EMPulse cannons with limited range fired by super weapon

:captiontag:`Type=EMPulse`
``````````````````````````

This type implements the super weapon known from :game:`Tiberian Sun`, with
several extensions. It makes one or more buildings, called cannons, of arbitrary
type fire at the same time at either a target location selected by the player or
at themselves.

.. note:: The AI cannot make full use of this super weapon yet, because it does
  not respect ranges, which is a fundamental feature of this super weapon type.

Default values for general tags:

:tagdef:`[SuperWeapon]SW.RangeMinimum=float - cell range`
  The minimum range below which a cannon is not eligible to fire. Set to
  negative values to use each cannon's primary weapon's minimum range. Defaults
  to :value:`0.0`, which disables the check.

:tagdef:`[SuperWeapon]SW.RangeMaximum=float - cell range`
  The maximum range above which a cannon is not eligible to fire. Set to
  negative values to use the each cannon's primary weapon's range. Defaults to
  :value:`-1.0`. 

:tagdef:`[SuperWeapon]SW.MaxCount=integer`
  The maximum number of cannons firing. Set to negative values for unlimited
  cannons. Defaults to :value:`1`. 

:tagdef:`[SuperWeapon]SW.AITargeting=enumeration`
  AI does not respect ranges. For :tag:`EMPulse.TargetSelf=yes` super weapons,
  use :value:`NoTarget` to enable AI players to use it. Defaults to
  :value:`None`.

:tagdef:`[SuperWeapon]Cursor=mouse cursor`
  Used when the target is in range of a cannon. Defaults to :value:`Attack`.

:tagdef:`[SuperWeapon]NoCursor=mouse cursor`
  Used when there is no cannon in range. Defaults to :value:`AttackOutOfRange`.

EMPulse specific tags:

:tagdef:`[SuperWeapon]EMPulse.Cannons=list of BuildingType`
  The building types considered to check the range and to fire. If the list is
  empty, all buildings with :tag:`EMPulseCannon=yes` are considered. All
  buildings are required to have a primary weapon. Defaults to :value:`none`.

:tagdef:`[SuperWeapon]EMPulse.TargetSelf=boolean`
  Whether each cannon to fire should fire its primary weapon at itself. The
  cannon does not actually fire; the weapon just detonates once on the cannon
  building immediately, similar to a death weapon. To actually damage itself,
  the building needs to have :tag:`DamageSelf=yes` set. Defaults to :value:`no`.

:tagdef:`[SuperWeapon]EMPulse.Linked=boolean`
  Whether only one cannon needs to satisfy the range checks to the target. All
  other cannons will then be considered regardless of range. Only makes sense if
  :tag:`SW.MaxCount` has a value other than :value:`1`. The difference to just
  making the cannon itself a designator is that the cannon can be made to not
  provide fire clearance on their own. Defaults to :value:`no`.

:tagdef:`[SuperWeapon]EMPulse.PulseBall=Animation`
  The optional animation played at the FLH at the beginning of the delay before
  the cannon fires. Use :value:`none` to disable the pulse ball. This does not
  disable the delay. Defaults to :value:`PULSBALL`.

:tagdef:`[SuperWeapon]EMPulse.PulseDelay=integer - frames`
  The delay before firing, but after the cannon rotated towards the target and
  started the :tag:`EMPulse.PulseBall` animation. Defaults to :value:`32`.

There are three firing modes opposed to the one known from :game:`Tiberian Sun`.
Buildings with :tag:`EMPulseCannon=yes` rotate their turret and then create a
single bullet using the primary weapon that is thrown at the target. The
building does not actually fire and several weapon effects are not respected.

If :tag:`EMPulse.TargetSelf=yes`, a single bullet is immediately detonated at
each firing cannon's location. Again, the building does not actually fire.

If a building with :tag:`EMPulseCannon=no` is put into :tag:`EMPulse.Cannons`,
the building will fire its primary weapon at the target directly, but without
charging or turret rotation, and without any further range checks. Thus, turrets
are not supported, and buildings are not guaranteed to fire at all if they
didn't rotate in the right direction before the super weapon is fired.

Other changes:

The pulse ball animation that was previously hardcoded to :value:`PULSBALL` has
now been made customizable and optional. If an :tag:`EMPulseCannon=yes` building
had a primary weapon without any valid :tag:`Report` set, the game would crash.
This does not happen anymore.

.. versionadded:: 0.8
