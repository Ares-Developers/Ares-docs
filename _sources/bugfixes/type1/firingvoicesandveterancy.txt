.. index:: Veterancy; Units won't lose their special weapon firing voices once they become elite.

===========================
Firing Voices and Veterancy
===========================
:game:`Yuri's Revenge` uses different unit voice lists for firing weapons
(:tag:`VoicePrimaryWeaponAttack`, :tag:`VoicePrimaryEliteWeaponAttack`,
:tag:`VoiceSecondaryWeaponAttack` and :tag:`VoiceSecondaryEliteWeaponAttack`).
If the :tag:`*EliteWeaponAttack` list is empty, :tag:`VoiceAttack` is used
instead of the more appropriate non-elite version :tag:`*WeaponAttack`.

This behavior makes units like Boris, Magnetrons, Siege Choppers, Boomers and
Floating Discs lose their special voices once they become elite. :game:`Ares`
falls back to the non-elite weapon firing voices instead of using the generic
:tag:`VoiceAttack` ones.

.. versionadded:: 0.2
  