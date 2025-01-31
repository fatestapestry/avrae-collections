# Ability name mapping
# use with e.g. ability_name = ABILITY_NAMES.get(ability.lower(), ability)
ABILITY_NAMES = {
    'str': 'Strength',
    'strength': 'Strength',
    'dex': 'Dexterity',
    'dexterity': 'Dexterity',
    'con': 'Constitution',
    'constitution': 'Constitution',
    'int': 'Intelligence',
    'intelligence': 'Intelligence',
    'wis': 'Wisdom',
    'wisdom': 'Wisdom',
    'cha': 'Charisma',
    'charisma': 'Charisma'
}

PROFICIENCY_LEVELS = {
    "none": [0, "Not Proficient"],
    "half": [0.5, "Half Proficient"],
    "pro": [1, "Proficient"],
    "exp": [2, "Expertise"]
}


def make_save_roll(character, ability, adv, bonuses=None):
    """Makes a save roll with advantage/bonuses"""
    roll_str = "2d20kh1" if adv == 1 else "2d20kl1" if adv == -1 else "1d20"
    roll_str += f"+{character.saves.get(ability).value}"

    if bonuses:
        roll_str += f"+{'+'.join(bonuses)}"

    result = vroll(roll_str)

    # Get natural roll - handling bold text
    dice_str = result.dice.split("(")[1].split(")")[0].replace('*', '')
    nat_roll = None
    if "," in dice_str:  # Advantage/Disadvantage roll
        for num in dice_str.split(","):
            if "~~" not in num:
                nat_roll = int(num.strip())
                break
    else:  # Normal roll
        nat_roll = int(dice_str.strip())

    return result, nat_roll


def embed_msg(title, desc=None, footer=None, field=None, fields=None):
    field_str = ""
    fields_str = ""
    if field:
        field_str = f'-f "{field}"'
    if fields:
        fields.insert(0, "")
        fields_str = " -f ".join([f'"{f}"' for f in fields])
    return f'embed -title "{title}" ' \
           f'-desc "{desc if desc else ""}" ' \
           f'{field_str if field_str else ""} ' \
           f'{fields_str if fields_str else ""} ' \
           f'-color <color> ' \
           f'-thumb <image> ' \
           f'-footer "{footer if footer else ""}"'


def is_in_combat(combat, footer=None):
    """Directly returns embed on failure"""
    if not combat:
        return embed_msg(
            title="Error",
            desc="Not in combat.",
            footer=footer
        )


def validate_targets(combat, targets, footer=None):
    """Directly returns embed on failure"""
    for target in targets:
        if not combat.get_combatant(target):
            return embed_msg(
                title="Error",
                desc=f"Error: Target `{target}` not found in combat.",
                footer=footer
            )


def apply_effect_to_targets(combat, targets, effect_name, effect_config):
    """
    Apply an effect to multiple targets.

    Args:
        combat: The combat instance
        targets: List of target names
        effect_name: Name of the effect
        effect_config: Dict containing effect configuration matching API spec
            (passive_effects, buttons, desc, etc.)

    Returns:
        List of tuples (target_name, description) where description indicates:
        - Effect was added ("Added effect...")
        - Effect already exists ("Already has effect...")

    Raises:
        ValueError: If effect_config is invalid
        RuntimeError: Any other failure in effect application, including effect data
    """
    results = []

    for target in targets:
        combatant = combat.get_combatant(target)

        # Check if effect exists
        if combatant.get_effect(effect_name):
            results.append((combatant.name, f"Already has the `{effect_name}` effect"))
            continue

        try:
            effect = combatant.add_effect(effect_name, **effect_config)
            results.append((combatant.name, f"Added effect `{effect_name}`"))
        except Exception as e:
            raise RuntimeError(f"Failed to apply effect to {combatant.name}: {str(e)}\nEffect config: {effect_config}")

    return results
