Campaign List
~~~~~~~~~~~~~

If you have more campaigns than the game's default Campaign Selection menu
supports you can switch to a campaign list as in :game:`Tiberian Sun`.
:game:`Ares` supports an arbitrary number of campaigns. Every non-debug battle
listed in :file:`battlemd.ini` will show up in the list under the name defined
by :tag:`Description=`.

.. image:: /images/ui_campaignlist.jpg
  :alt: Campaign list showing both original campaigns with summary
  :align: center

Enable the campaign list in :file:`uimd.ini`:

:tagdef:`[UISettings]CampaignList=boolean`
  Enables the campaign list instead of the game's default menu. Defaults to
  :value:`no`.
:tagdef:`[UISettings]CampaignListSize=integer`
  The number of campaigns shown in the Campaign list without scrolling. The
  number of campaigns shown cannot be less than :value:`3`. The maximum number
  depends on :tag:`ShowSummary`. Defaults to :value:`7`.
:tagdef:`[UISettings]ShowSummary=boolean`
  Whether the campaign list displays a campaign's :tag:`Summary` below the
  difficulty selection. If shown, the maximum campaign list size is :value:`14`,
  otherwise it is :value:`18`. Defaults to :value:`yes`.
:tagdef:`[UISettings]ShowDebugCampaigns=boolean`
  Also displays campaigns in the list that have `DebugOnly=yes` set. Defaults to
  :value:`no`.


You can customize the campaigns in the list by editing :file:`battlemd.ini`:

:tagdef:`[Battle]HoverSound=sound`
  The sound to be played when the player selects a campaign. This defaults to
  :value:`AlliedCampaignSelect`, :value:`SovietCampaignSelect`, and
  :value:`BootCampSelect` for the original in-game campaigns. The selection menu
  plays them when the mouse hovers over the respective campaign's image.
:tagdef:`[Battle]Summary=CSF label`
  Provide an optional summary of the campaign's or mission's story. It will be
  shown below the difficulty slider if not disabled using
  :tag:`[UISettings]ShowSummary`.

.. index:: Interface; Campaign list

.. versionadded:: 0.2
.. versionchanged:: 0.9
