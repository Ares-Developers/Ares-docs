.. index:: Warheads; Override die sounds and voices

Override Die Sounds and Voices
``````````````````````````````

When killing units using this warhead, the die sounds and voices can be
overridden to not give owning players a clue that their units are under attack,
or to disable these sounds for warheads that should not be considered killing
units like Make Infantry conversions.

:tagdef:`[Warhead]DieSound.Override=soundmd entry`
  The sound to use when an object is destroyed by this warhead. Objects that
  have no :tag:`DieSound` will not play anything. Use :value:`<none>` to
  suppress :tag:`DieSound`.

:tagdef:`[Warhead]VoiceDie.Override=soundmd entry`
  The voice to use when an object is destroyed by this warhead. Objects that
  have no :tag:`VoiceDie` will not play anything. Use :value:`<none>` to
  suppress :tag:`VoiceDie`.

.. versionadded:: 3.0
