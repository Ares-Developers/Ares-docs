.. index::
  Weapons; RadBeams and waves will use the correct FLH (instead of always using PrimaryFLH)
  Changes; RadBeams and waves will use the correct FLH (instead of always using PrimaryFLH)

======================================
RadBeams And Waves Using The Wrong FLH
======================================

The weapon effects of Radiation Beams and Waves (Sonic and Magnetron Beams)
would always get drawn from the FLH of the firing unit's current primary weapon
rather than from the FLH of the weapon that actually fired the beam/wave. Now
the weapon effects will be drawn using the correct FLH.

.. note:: The Magnetron (:tag:`[TELE]`) does not have a :tag:`SecondaryFireFLH`
  set in the unmodded game, so any mod using :game:`Ares` will need to set this
  themselves. You may also need to correct the FLHs for the IFV (:tag:`[FV]`).

.. versionadded:: 0.1
