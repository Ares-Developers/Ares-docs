:captiontag:`Type=Firestorm`
````````````````````````````

This super weapon is a recreation of the :game:`Tiberian Sun` Firestorm Defense
System. For more details, see :doc:`Firestorm Wall </restored/firestormwall>`.

This super weapon uses the Charge/Drain logic: once activated, the effect
will persist for a duration determined by :tag:`SW.ChargeToDrainRatio`, after
which it will automatically shut down and the superweapon will restart its
charging process.

Whilst the effect is active, players can click the super weapon button again to
manually deactivate it, thus allowing the recharge process to begin earlier and
finish faster. See :ref:`Charge/Drain <charge-drain-sw>`, or refer to `ModEnc
<http://modenc.renegadeprojects.com/ChargeToDrainRatio>`_ for more information
about Charge/Drain logic.

In :game:`Tiberian Sun`, the Charge/Drain feature was disableable through an
INI flag (:tag:`[SuperWeapon]UseChargeDrain=no`) however: :game:`Ares` forces
this logic to be used regardless of the value of that flag. :game:`Ares` also
forces this super weapon to ignore its assigned :tag:`Action`, if any, as this
is required to make it activate from a single click of the sidebar icon.

.. note:: The AI will not use this super weapon. In missions, it is possible to
  control the Firestorm using the map actions 92 and 93.

.. index:: Super Weapons; Firestorm Wall

.. versionadded:: 0.1
.. versionchanged:: 0.A
