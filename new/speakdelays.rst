.. index::
  EVA; SpeakDelays for cloaked and subterranean units
  Cloak; EVA Speak Delay
  Subterranean; EVA Speak Delay

Speak Delays
~~~~~~~~~~~~

EVA announces every time when a cloaked or subterranean unit has been detected.
This is unlike the low power or insufficient funds notice, that will occur only
once in a while, defined by the setting :tag:`[AudioVisual]SpeakDelay`.
:game:`Ares` adds distinct speak delays for the unit detectiion notices.

:tagdef:`[AudioVisual]StealthSpeakDelay=double - minutes`
  Minutes between EVA repeating the warning that a stealth unit has been
  detected. Defaults to :value:`0.0`.
:tagdef:`[AudioVisual]SubterraneanSpeakDelay=double - minutes`
  Minutes between EVA repeating the warning that a subterranean unit has been
  detected. Defaults to :value:`0.0`.

.. versionadded:: 2.0
