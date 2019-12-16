.. index:: TechnoTypes; Convert one unit type into another

Type Conversion
===============

To a limited extent, it is possible to change the type of a unit in certain
conditions. Supported are only unit to unit, infantry to infantry, and aircraft
to aircraft. This is not supported for buildings.

There is one rule to follow, which is easily stated but difficult to adhere to:
**a unit is not allowed to convert into another type that has a chance to
currently be in a position where the new type cannot be**. For example if an
infantry unit gets bigger while inside a full open topped transport, the
converted type not being allowed as passenger or occupant. This also works
backwards: a vehicle cannot lose its ability to hold passengers.

A unit that has not been created with a temporal weapon, a mind control weapon,
or a parasite weapon cannot gain such by changing the type.

The following are fully supported:

+ changing :tag:`Strength` will keep the units health the same
+ changing :tag:`Armor`
+ Ammo is reduced if new type has less :tag:`Ammo`
+ :tag:`Cloakable` is applied again
+ Spotlight is removed or created
+ AttachEffect on the type is removed or created
+ :tag:`ROT` and :tag:`TurretROT` are reset
+ All prerequisites are rechecked once a unit converts

.. note:: Converted units no longer count as original units for
  :tag:`BuildLimit` checks. As with all other prerequisite checks, units will
  not be disallowed to convert, even if it violates :tag:`BuildLimit` rules.

.. versionadded:: 2.0


.. index:: TechnoTypes; Type change on promotion

On Promotion
------------

The unit type can be changed by promotion, not only allowing for more than the
usual three veterancy levels, but also allowing to change several of the unit's
attributes including their appearance.

Note that if the unit skips the veteran rank and becomes elite immediately,
Veteran settings are not applied. Also note that this is not cascading: if a
unit is promoted to elite and converts to a veteran version of another type,
which in turn should convert to something else, no further conversion takes
place.

:tagdef:`[TechnoType]Promote.VeteranType=TechnoType`
  If set, the unit converts into this type when being promoted to veteran rank.
  Defaults to :value:`none`.

:tagdef:`[TechnoType]Promote.EliteType=TechnoType`
  If set, the unit converts into this type when being promoted to elite rank.
  Defaults to :value:`none`.

The following tags can be used to promote a unit to a rookie of another type.
Using :value:`-1.0` removes one rank, thus a unit becoming veteran gets one rank
removed and essentially ends as a rookie of the converted type, while a unit
becoming elite gets one rank removed and essentially becomes a veteran of the
converted type. :value:`-2.0` would make the latter a rookie, too.

:tagdef:`[TechnoType]Promote.VeteranExperience=double`
  A value added to the experience when a unit type is converted using
  :tag:`Promote.VeteranType`. Defaults to :value:`0.0`.

:tagdef:`[TechnoType]Promote.EliteExperience=double`
  A value added to the experience when a unit type is converted using
  :tag:`Promote.EliteType`. Defaults to :value:`0.0`.

.. versionadded:: 2.0


.. index:: TechnoTypes; Type change when deploying

Via :captiontag:`IsSimpleDeployer`
----------------------------------

Unit can simple-deploy into another type. Unlike in the original game the unit
will be movable after deploying, opposed to being locked in place like the
original Siege Chopper.

:tag:`DeployingAnim` is optional. If not present, units will convert types
immediately, without turning their facing to :tag:`DeployDir`. See
:doc:`DeployDir </new/deploydir>`.

:game:`Ares` extends :tag:`IsSimpleDeployer` logic to allow deploying units not
on the ground. Also, :tag:`DeployToLand` has been extended to also work on units
using the Hover locomotor. If :value:`yes`, units will land, also respecting
:tag:`DeployDir`.

Because this conversion always happens with the unit being present on the map
and guaranteed to be standing still, settings like :tag:`Locomotor` and
:tag:`Size` can be changed within reasonable limits.

:tagdef:`[TechnoType]Convert.Deploy=TechnoType`
  The type a :tag:`IsSimpleDeployer=yes` unit deploys into. This converts the
  type after deploying completed, and after the optional :tag:`DeployingAnim`
  has finished playing. Defaults to :value:`none`.

.. versionadded:: 2.0


.. index:: TechnoTypes; Type change when entering water

When Transitioning Between Land and Water
-----------------------------------------

The tag :tag:`WaterImage` allows to render a unit differently when it is on
water, which was used on the GDI APC in :game:`Tiberian Sun`. The following
settings allow to change a unit's type. This way, the unit could change image,
weapons, armor and so on.

.. note:: Water and Land units should not define a conversion to their own type,
  like a water unit converting into an other water unit.

:tagdef:`[TechnoType]Convert.Water=TechnoType`
  The type to convert to when a unit moves onto a beach or water cell. Defaults
  to :value:`none`.

:tagdef:`[TechnoType]Convert.Land=TechnoType`
  The type to convert to when a unit moves onto a cell that's neither beach nor
  water. Defaults to :value:`none`.

.. versionadded:: 2.0
