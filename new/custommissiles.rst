Custom Missiles
~~~~~~~~~~~~~~~

:game:`Ares` allows you to create new missile types and customize the existing
types (:tag:`V3RocketType`, :tag:`DMislType`, :tag:`CMislType`). Missiles are
:type:`AircraftTypes` which have special logic attached to behave like a
projectile launched from another unit and carrying a warhead to its target.

Instead of defining the missile settings in the :tag:`[General]` section,
:game:`Ares` allows you to put them directly on the :type:`AircraftType`. Apart
from that, the missiles work the same way the original launcher/missile pairs
work. This allows you to create an arbitrary number of new missiles.

:tagdef:`[AircraftType]Missile.Custom=boolean`
  Specifies whether this :type:`AircraftType` should exhibit missile behavior.
  If set to :value:`yes` it enables the missile tags listed below, which must
  be set to meaningful values. Not recommended on :tag:`V3RocketType`,
  :tag:`DMislType` and :tag:`CMislType`. Defaults to :value:`no`.

  .. note:: If you intend to override the original missiles defined as
    \ :tag:`V3RocketType`, :tag:`DMislType` and :tag:`CMislType`, you also have
    to define the following tags. :game:`Ares` will not default to the original
    game tags for these types defined in the :tag:`[General]` section.

The following tags are used only if :tag:`[AircraftType]Missile.Custom=yes` is
set.

:tagdef:`[AircraftType]Missile.PauseFrames=integer`
  Defines how many frames the missile pauses on the launching unit before
  tilting. Defaults to :value:`0`.

:tagdef:`[AircraftType]Missile.TiltFrames=integer`
  Defines how many frames it takes for the missile to tilt to firing position.
  Defaults to :value:`0`.

:tagdef:`[AircraftType]Missile.PitchInitial=float`
  Defines the starting pitch of the missile before tilting up. Valid range is
  :value:`0.0` (horizontal) to :value:`1.0` (vertical). Defaults to
  :value:`0.0`.

:tagdef:`[AircraftType]Missile.PitchFinal=float`
  Defines the ending pitch of the missile after tilting up and when firing.
  Valid range is :value:`0.0` (horizontal) to :value:`1.0` (vertical).
  Defaults to :value:`0.0`.

:tagdef:`[AircraftType]Missile.TurnRate=float`
  Defines the pitch maneuverability of the missile in air. See original
  missiles for examples. Valid range is :value:`0.0` to :value:`1.0`. Defaults
  to :value:`0.0`.

:tagdef:`[AircraftType]Missile.RaiseRate=float`
  Defines how much the missile will raise each turn on the launching unit.
  Defaults to :value:`0.0`.

:tagdef:`[AircraftType]Missile.Acceleration=float`
  Defines how much is added to the missile's velocity each frame during launch.
  Defaults to :value:`0.0`.

:tagdef:`[AircraftType]Missile.Altitude=integer`
  Defines the cruising altitude in leptons at which height missile begins
  leveling off. Defaults to :value:`0`.

:tagdef:`[AircraftType]Missile.Damage=integer`
  Defines how much damage the missile does when launched from a rookie or
  veteran unit. Defaults to :value:`0`.

:tagdef:`[AircraftType]Missile.EliteDamage=integer`
  Defines how much damage the missile does when launched from an elite unit.
  Defaults to :value:`0`.

:tagdef:`[AircraftType]Missile.BodyLength=integer`
  Defines how long the body of the missile is in leptons. This is used to draw
  the trailer. Defaults to :value:`0`.

:tagdef:`[AircraftType]Missile.LazyCurve=boolean`
  Whether the missile's path is a ballistic curve like the original V3 rocket.
  Otherwise the missile maintains the defined altitude. Defaults to
  :value:`no`.

:tagdef:`[AircraftType]Missile.Warhead=Warhead`
  Defines the warhead the missile uses to deliver damage when launching from
  a rookie or veteran unit. Defaults to :value:`none`.

:tagdef:`[AircraftType]Missile.EliteWarhead=Warhead`
  Defines the warhead the missile uses to deliver damage when launching from
  an elite unit. Defaults to :value:`none`.

Aside from the missile settings you can customize the takeoff and trailer
animations. These settings can be used for any missile, whether they are custom
or not. :game:`Ares` also optimizes away the lookup of the animation types,
thus it does not happen each time a new animation is to be created for each
missile.

:tagdef:`[AircraftType]Missile.TakeOffAnim=Animation`
  Defines the optional animation played when the missile takes off. Defaults to
  :value:`V3TAKOFF`.

:tagdef:`[AircraftType]Missile.TrailerAnim=Animation`
  Defines the optional animation that is used to draw the trailer of this
  missile. Defaults to :value:`V3TRAIL`.

:tagdef:`[AircraftType]Missile.TrailerSeparation=integer`
  Defines the number of frames to the creation of another trailer animation.
  Defaults to :value:`3`.

.. index:: Missiles; Add new and customize the original missile types.

.. versionadded:: 0.3
