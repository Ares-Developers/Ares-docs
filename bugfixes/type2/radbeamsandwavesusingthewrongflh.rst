RadBeams And Waves Using The Wrong FLH
``````````````````````````````````````

The weapon effects of Radiation Beams and Waves (Sonic and Magnetron
Beams) would always get drawn from the FLH of the firing unit's
current primary weapon rather than from the FLH of the weapon that
actually fired the beam/wave. Now the weapon effects will be drawn
using the correct FLH.

Note that the Magnetron does not have a `SecondaryFireFLH` set in the
unmodded game, so any mod using Ares will need to set this themselves.
You may also need to correct the FLHs for the IFV. RadBeams and waves
will use the correct FLH (instead of always using PrimaryFLH).

.. versionadded:: 0.1



<<<SEPARATOR>>>
