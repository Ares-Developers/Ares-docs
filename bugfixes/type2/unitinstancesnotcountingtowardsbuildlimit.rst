.. index::
  BuildLimit; Vehicles that deploy into a building now count towards the BuildLimit of that building and vice versa
  BuildLimit; Hijackers inside vehicles now count towards that hijacker's BuildLimit
  BuildLimit; AirportBound aircraft did not respect BuildLimit
  Vehicle Thief; Hijackers inside vehicles now count towards that hijacker's BuildLimit
  Aircraft; AirportBound aircraft did not respect BuildLimit

============================================================
Unit Instances Not Counting Towards :captiontag:`BuildLimit`
============================================================

If you have a vehicle which deploys into a structure, both the deploying vehicle
and the structures will now count towards the :tag:`BuildLimit` of that vehicle
and that structure.

Hijackers inside stolen vehicles now count towards the Hijacker's
:tag:`BuildLimit`.

:tag:`AirportBound` aircraft did not respect :tag:`BuildLimit` and players could
build as many of them as there were free docks. Now :tag:`BuildLimit` is also
respected.

.. versionadded:: 0.1
.. versionchanged:: 0.A
