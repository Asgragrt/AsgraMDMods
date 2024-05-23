# Change env before running

from jinja2 import Template
import codecs

#create an dict will all data that will be populate the template
mods = {}
mods['mods'] = [
  'https://github.com/MDMods/CurrentCombination',
  'https://github.com/MDMods/SelectiveEffects',
  'https://github.com/MDMods/FadeIn',
  'https://github.com/MDMods/StricterJudge',
  'https://github.com/Asgragrt/RomajiSongName',
  'https://github.com/Asgragrt/UnlockSpecialWelcomeScreens',
  'https://github.com/Asgragrt/MenuCharacter',
  'https://github.com/Asgragrt/PeroPeroSkip',
  'https://github.com/Asgragrt/WelcomeSurprise'
]

def linkToDict(link: str) -> dict:
    splitted = link.split('/')
    return { 'link': link, 'name': splitted[-1] }

mods['mods'] = list(map(linkToDict, mods['mods']))


#render the template
with open('template.md', 'r') as file:
  template = Template(file.read(),trim_blocks=True)
rendered_file = template.render(mods=mods)

#output the file
output_file = codecs.open("README.md", "w", "utf-8")
output_file.write(rendered_file)
output_file.close()