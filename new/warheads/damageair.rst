Damage Airborne Units
`````````````````````

Warheads detonation on the ground cause explosions that never affect units in
the air, no matter how large the :tag:`CellSpead` range is. If a warhead
detonated just a few leptons above the ground however, airborne units would be
affected if they were in range. This can now be changed.

:tagdef:`[Warhead]DamageAirThreshold=integer - leptons`
  If the warhead detonates *more* than this many leptons above the ground, units
  in the air will be affected. Otherwise, units in the air are not damaged.
  Defaults to :value:`0`.

  .. quickstart:: Use :value:`-1` to damage even air units when the warhead
    detonates on the ground, or a high positive value like :value:`9999` to
    disable damaging air units despite the warhead detonating in air.

:tagdef:`[General]DamageAirConsiderBridges=boolean`
  Whether a warhead detonating above a bridge will consider the bridge's height
  for finding out whether units in air are to be damaged. Defaults to
  :value:`no`.

  If :value:`no`, a warhead detonating on a bridge will be considered to be four
  levels (416 leptons) high in the air, if :value:`yes`, it will be 0 leptons
  above the ground and thus by default not trigger damaging units in the air. 

.. index:: Warheads; Damage or don't damage units in the air

.. versionadded:: 0.B
