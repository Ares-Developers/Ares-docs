Nuke Flash
``````````

The :type:`WarheadType` called :tag:`NUKE` has hardcoded behavior to create a
map wide flash when detonating. This effect has been made customizable, so it
can be enabled for other warheads, too, or disabled for :tag:`NUKE`.

.. warning:: Use this effect responsibly. Having overlapping effects does not
  work too well.

:tagdef:`[Warhead]NukeFlash.Duration=integer - frames`
  The number of frames the nuke flash fades in and stays fully active before it
  fades out again. A value of :value:`0` disables the effect. Defaults to
  :value:`30` for :tag:`NUKE`, to :value:`0` otherwise.

.. index:: Warheads; Nuke Flash

.. versionadded:: 0.E
