.. index::
  Occupiers; Buildings that can't be assaulted
  Assaulter; Different levels of protection
  Buildings; Protect occupants against assault

Assaulter
~~~~~~~~~

The :tag:`Assaulter` logic can be customized with the following tag, to make
certain buildings unassaultable, or to create infantry that can even assault
specially protected buildings.

:tagdef:`[TechnoType]Assaulter.Level=integer`
  Defines the levels compared when an :tag:`Assaulter=yes` infantry is to
  assault building. Infantry can only assault buildings with levels less than
  or equal to their own level. Defaults to :value:`0`.

.. note:: Buildings with :tag:`Assaulter.Level` < :value:`0` are not
  assaultable.

.. versionadded:: 0.A
