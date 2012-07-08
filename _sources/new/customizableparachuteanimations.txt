Customizable Parachute Animations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Units can now have their own individual parachute animation.

:tagdef:`[TechnoType]Parachute.Anim=animation`
  Specifies the animation from :file:`artmd.ini` to use as the unit's parachute
  when the it is falling. If omitted, :tag:`Parachute.Anim` will default to
  :value:`PARACH`. The SHP is expected to be in the unit palette.


While the animation is playing, the units's falling speed will reach, but not
exceed, :tag:`[General]ParachuteMaxFallRate=`. After the animation disappears,
if the unit is still falling then the object's speed will increase to match
:tag:`[General]NoParachuteMaxFallRate=`.

.. index:: Art; Custom parachute animations.

.. versionadded:: 0.1
