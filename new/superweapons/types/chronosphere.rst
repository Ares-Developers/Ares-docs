.. _chronosphere:

:captiontag:`Type=ChronoSphere`
```````````````````````````````

The :value:`ChronoSphere` type super weapon needs a :value:`ChronoWarp` type
super weapon. If you have more than one :value:`ChronoSphere` super weapons, you
can reuse the same :value:`ChronoWarp` super weapon for all of them, or create
dedicated super weapons if you want to. See :ref:`SW.PostDependent
<sw-postdependent>`.

Default values for general tags:

:tagdef:`[SuperWeapon]SW.Range=float,integer`
  Range affected by the chronoshift. Defaults to :value:`3,3`.
:tagdef:`[SuperWeapon]SW.Animation=Animation`
  The placement animation indicating the source location for the chronoshift.
  Defaults to :tag:`[General]ChronoPlacement`.
:tagdef:`[SuperWeapon]SW.AnimationHeight=integer`
  The height the :tag:`SW.Animation` is played above the ground. Defaults to
  :value:`5`.
:tagdef:`[SuperWeapon]SW.AITargeting=enum`
  Defaults to :value:`none`. The AI cannot use this.
:tagdef:`[SuperWeapon]SW.AffectsHouse=enum`
  Specifies the houses affected by the chronoshift. Defaults to :value:`all`.
:tagdef:`[SuperWeapon]SW.AffectsTarget=enum`
  Specifies which types the chronoshift affects. Defaults to
  :value:`infantry,units`.
  
  .. note:: Please note that buildings with :tag:`Chronoshift.IsVehicle=yes` are
    considered units and not buildings, if
    \ :tag:`Chronosphere.ReconsiderBuildings=yes` is set.
:tagdef:`[SuperWeapon]SW.PostDependent=super weapon`
  Specifies the super weapon used to select the target cell for the chronoshift
  by ID. Defaults to the first :value:`ChronoWarp` type super weapon in the
  :type:`SuperWeaponTypes` list.


Chronosphere specific tags:

:tagdef:`[SuperWeapon]Chronosphere.BlastSrc=Animation`
  The Animation played above the source when the chronoshift is started.
  Defaults to :tag:`[General]ChronoBlast`.
:tagdef:`[SuperWeapon]Chronosphere.BlastDest=Animation`
  The Animation played above the destination when the chronoshift is started.
  Defaults to :tag:`[General]ChronoBlastDest`.
:tagdef:`[SuperWeapon]Chronosphere.ReconsiderBuildings=boolean`
  Defines whether the chronoshift will consider buildings with
  :tag:`Chronoshift.IsVehicle=yes` as vehicles instead. Otherwise
  deployed-vehicle type buildings always count as buildings like with the
  original Chronosphere. Defaults to :value:`yes`.
:tagdef:`[SuperWeapon]Chronosphere.KillOrganic=boolean`
  Defines whether the chronoshift will kill all organic units. Otherwise the
  units will not be killed by the chronoshift and teleport instead. Defaults to
  :value:`yes`.
:tagdef:`[SuperWeapon]Chronosphere.KillTeleporters=boolean`
  Defines whether the chronoshift will kill units with :tag:`Teleporter=yes`
  set. Otherwise the units will be chronoshifted. Defaults to :value:`no`.
:tagdef:`[SuperWeapon]Chronosphere.AffectsIronCurtain=boolean`
  Defines whether the chronoshift will affect iron curtained units. Otherwise
  the units will be ignored. Defaults to :tag:`no`.
:tagdef:`[SuperWeapon]Chronosphere.AffectsUnwarpable=boolean`
  Defines whether the chronoshift will affect units with :tag:`Warpable=no` set.
  Otherwise the units will be ignored. Defaults to :tag:`yes`.
:tagdef:`[SuperWeapon]Chronosphere.AffectsUndeployable=boolean`
  Defines whether the chronoshift will affect buildings that can be undeployed
  into units again. Effectively, if a building has :tag:`UndeploysInto=` set and
  this value is :value:`yes`, :tag:`SW.AffectsTarget` and
  :tag:`Chronoshift.IsVehicle` are bypassed and the building is chronoshifted
  with vehicle placement rules. Defaults to :value:`no`.

  .. note:: "Undeployable" means *buildings that can undeploy*, rather than
    "vehicles that cannot deploy".

:tagdef:`[SuperWeapon]Chronosphere.BlowUnplaceable=boolean`
  Defines whether the chronoshift will destroy buildings that don't fit in the
  target location, otherwise the buildings will stay at the source location.
  This function will not spare units that have been deployed into buildings.
  Defaults to :value:`yes`.


Other changes:

It is now possible to chronoshift buildings. Note that there is a difference to
chronoporting units: If a building cannot be placed in the target location it
will blow up in the source location (if the default
:tag:`Chronosphere.BlowUnplaceable=yes` is used). Vehicle-type buildings will
try to find a fitting place just like units would.

See :doc:`Chronoshift </new/chronoshift>` to prevent objects from being
chronoshifted.

.. warning:: There are several known issues with chronoshifting buildings that
  haven't been fixed yet. For example, buildup animations will restart and the
  turret facing is reset.

.. versionadded:: 0.2


:captiontag:`Type=ChronoWarp`
`````````````````````````````

The :tag:`ChronoWarp` type super weapon is fired at the target location of the
chronoshift and marks the position the units will be teleported to. If you have
a :value:`ChronoSphere` type super weapon you have to have one
:value:`ChronoWarp` type super weapon, too.

From the :value:`ChronoWarp` type super weapon only the targeting and cursor
properties are used, as well as :value:`Range` to indicate the area of effect by
drawing radial lines around the cursor. :tag:`SW.Range` is not used.

For the actual chronoshifting tags, see :ref:`ChronoSphere <chronosphere>`.

.. versionadded:: 0.2
