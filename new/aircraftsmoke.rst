Aircraft Smoke
~~~~~~~~~~~~~~

When aircraft creates a smoke trail because of heavy damage, the animation used
is hardcoded and the same for all :type:`AircraftTypes`, yet it is looked up
each time anew for every aircraft anyhow. When an aircraft is destroyed, it
creates lots of smoke animations. This fix gets rid of the superfluous lookup.
Additionally, the smoke has been made customizable per :type:`AircraftType`.

:tagdef:`[AircraftType]Smoke.Anim=animation`
  The animation created as smoke trailer. Defaults to :value:`SGRYSMK1`.

:tagdef:`[AircraftType]Smoke.ChanceRed=integer - percent`
  The chance of a heavily damaged aircraft creating a smoke animation each
  frame. Defaults to :value:`10`.

:tagdef:`[AircraftType]Smoke.ChanceDead=integer - percent`
  The chance of a crashing aircraft creating a smoke animation each frame.
  Defaults to :value:`80`.

.. index:: Aircraft; Smoke animation

.. versionadded:: 0.7
