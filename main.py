"""Generate the proper README file from a template"""

# Change env before running

import codecs
from jinja2 import Template


def link_to_dict(link: str) -> dict:
    """Split a github link to get the repo name and save it to a dictionary"""
    splitted = link.split("/")
    return {"link": link, "name": splitted[-1]}


def main():
    """Main function"""
    # Create a dict with all data that will be populate the template
    mods = {}
    mods["mods"] = [
        "https://github.com/MDMods/CurrentCombination",
        "https://github.com/MDMods/SelectiveEffects",
        "https://github.com/MDMods/FadeIn",
        "https://github.com/MDMods/StricterJudge",
        "https://github.com/Asgragrt/RomajiSongName",
        "https://github.com/Asgragrt/UnlockSpecialWelcomeScreens",
        "https://github.com/Asgragrt/MenuCharacter",
        "https://github.com/Asgragrt/PeroPeroSkip",
        "https://github.com/Asgragrt/WelcomeSurprise",
    ]

    mods["mods"] = list(map(link_to_dict, mods["mods"]))

    # render the template
    with open("template.md", "r", encoding="utf-8") as file:
        template = Template(file.read(), trim_blocks=True)
    rendered_file = template.render(mods=mods)

    # output the file
    with codecs.open("README.md", "w", "utf-8") as file:
        file.write(rendered_file)
        file.close()


if __name__ == "__main__":
    main()
