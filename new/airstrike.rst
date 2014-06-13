Airstrike Voices
~~~~~~~~~~~~~~~~

:game:`Ares` supports custom airstrike related voices. These flags can be
defined on the designator unit like Boris and the aircraft (the designator's
flags take precedence). If a flag isn't set on any of those, the respective
:tag:`[AudioVisual]` flag is used. To disable an airstrike voice, set it to an
empty sound.

:tagdef:`[TechnoType]VoiceAirstrikeAttack=soundmd entry`
  Specifies the voice played when the airstrike is called in and the team enters
  the map. Defaults to :tag:`AirstrikeAttackVoice`.

:tagdef:`[TechnoType]VoiceAirstrikeAbort=soundmd entry`
  Specifies the voice played when the designator unit is killed before the
  aircraft had a chance to fire. Defaults to :tag:`AirstrikeAbortSound`.

.. index:: Airstrikes; Custom attack and abort voices.

.. versionadded:: 0.7
