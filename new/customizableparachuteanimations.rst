Customizable Parachute Animations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Objects can now have their own individual parachute animation.

:[Object]Parachute.Anim= (animation): Specifies the animation from
  artmd.ini to use as the object's parachute when the object is falling.
  If omitted, `Parachute.Anim` will default to PARACH. The SHP is
  expected to be in the unit palette. Parachute.Anim=


While the animation is playing, the object's falling speed will reach,
but not exceed, `[General]ParachuteMaxFallRate=`. After the animation
disappears, if the object is still falling then the object's speed
will increase to match `[General]NoParachuteMaxFallRate=`. Custom
parachute animations.

.. versionadded:: 0.1



<<<SEPARATOR>>>
