Mod-specific Information
~~~~~~~~~~~~~~~~~~~~~~~~

The following settings describe your mod and give it a name and a version
number to uniquely identify your mod. These tags are important for savegames to
distinguish files from different mods or different versions of the same mod, and
they are also printed out in :file:`debug.log` to aid diagnosing problems.

It is highly recommended to set those to meaningful individual values.

Both can be defined in :file:`uimd.ini`:

:tagdef:`[VersionInfo]Name=string`
  The name of the modification in unspecified format. Maximum 63 characters.
  Defaults to :value:`Yuri's Revenge`.
:tagdef:`[VersionInfo]Version=string`
  The version of the modification in unspecified format. Maximum 63 characters.
  Defaults to :value:`1.001`.

.. index:: Mods; Specify mod name and version

.. versionadded:: 0.8
