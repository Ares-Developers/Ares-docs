.. index::
  Vehicles; More than 8 facings for SHP units
  Facings; More than 8 facings for SHP units

:captiontag:`Facings` on Units
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:game:`Ares` supports to have more than just 8 facings for :type:`VehicleTypes`.
Set in :file:`artmd.ini`:

:tagdef:`[VehicleType]Facings=integer`
  The number of facings used for SHP based units. Supports powers of 2 equal to
  or larger than :value:`8`. Values less than :value:`8` result in only the
  first frame being used. Defaults to :value:`8`.

.. versionadded:: 0.9
