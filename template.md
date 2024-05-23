# Asgra's Muse Dash Mods

{% set basePinURL = 'https://github-readme-stats-asgra.vercel.app/api/pin/?username=asgragrt&repo={}&theme=vision-friendly-dark' %}
{% set basePinTemplate = '[![{}]({})]({})' %}

| Mod Name | Pin |
| --- | --- |
{% for mod in mods.mods %}
{% set pinURL = basePinURL.format(mod.name) %}
{% set pin = basePinTemplate.format(mod.name, pinURL, mod.link) %}
| [{{ mod.name }}]({{ mod.link }}) | {{ pin }} |
{% endfor %}