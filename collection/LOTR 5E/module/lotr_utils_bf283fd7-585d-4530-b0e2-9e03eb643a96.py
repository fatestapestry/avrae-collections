# lotr 5e metadata gvars
METADATA_SHADOW = "4160bb62-8791-4239-941c-b7805e5351b6"
METADATA_CHECK = "856f9b7a-c299-4052-9e7f-5fcba2f919be"
METADATA_JOURNEY = "a6e3208c-b3c8-408b-b310-43e3daab5332"

# utils gvars
UTILS_COMMON = "0c6d5bca-a15d-4e45-a08d-48cf51411088"

# Status Constants
STATUS_NORMAL = "Normal"
STATUS_ANGUISHED = "Anguished"
STATUS_MISERABLE = "Miserable"

# Counter Names
CC_SHADOW_POINTS = "Shadow Points"
CC_SHADOW_SCARS = "Shadow Scars"

# cvars
SHADOW_PATH = "lotrShadowPath"
LOTR_SKILLS = "lotrSkills"

# snippet params
MULTIPLE_ROLES_PENALTY = -5
BLESSING_DIE = {
    2: "1d4",
    3: "1d6",
    4: "1d8"
}

# footers
FOOTER_SHADOW = "!help lotrshadow for more info | Developed by @noralf#0"
FOOTER_CHECK = "!help lotrcheck for more info | Developed by @noralf#0"
FOOTER_EVENT = "!help lotrevent for more info | Developed by @noralf#0"
FOOTER_FATIGUE = "!help lotrfatigue for more info | Developed by @noralf#0"
FOOTER_FELL = "!help fell for more info | Developed by @noralf#0"
FOOTER_REINFORCED = "!help reinforced for more info | Developed by @noralf#0"

using(
    common_utils=UTILS_COMMON
)


def get_shadow_status(ch):
    """Gets current shadow points and state"""
    pts = ch.get_cc(CC_SHADOW_POINTS)

    if pts >= ch.stats.wisdom:
        return pts, STATUS_ANGUISHED
    if pts >= ceil(ch.stats.wisdom / 2):
        return pts, STATUS_MISERABLE
    return pts, STATUS_NORMAL


def create_full_shadow_display(ch, title, prefix_desc=None):
    """Creates the full status display with path and thresholds, optionally with prefix text"""
    shadow_points = ch.get_cc(CC_SHADOW_POINTS)
    shadow_scars = ch.get_cc(CC_SHADOW_SCARS)
    total, status = get_shadow_status(ch)
    footer = FOOTER_SHADOW

    # Load shadow path information
    shadow_path = load_json(ch.get_cvar(SHADOW_PATH))
    flaws_display = "None" if not shadow_path["currentFlaws"] else ", ".join(shadow_path["currentFlaws"])

    desc = (f"**Shadow Path**\n"
            f"* Calling: {shadow_path['calling']}\n"
            f"* Path: {shadow_path['path']}\n"
            f"* Flaws: {flaws_display}\n\n"
            f"**Current**\n"
            f"* Shadow Points: {shadow_points}/{ch.stats.wisdom}\n"
            f"* Shadow Scars: {shadow_scars}\n"
            f"* Status: {status}\n\n"
            f"**Shadow Thresholds**\n"
            f"* Miserable at: {ceil(ch.stats.wisdom / 2)} points\n"
            f"* Anguished at: {ch.stats.wisdom} points")
    if prefix_desc:
        desc = f"{prefix_desc}\n\n{desc}"
    return common_utils.embed_msg(title=title, desc=desc, footer=footer)


def create_brief_shadow_display(ch, title, prefix_desc=None):
    """Creates brief shadow status display, optionally with prefix text"""
    shadow_points = ch.get_cc(CC_SHADOW_POINTS)
    shadow_scars = ch.get_cc(CC_SHADOW_SCARS)
    total, status = get_shadow_status(ch)
    footer = FOOTER_SHADOW

    stats = (f"**Current**\n"
             f"* Shadow Points: {shadow_points}/{ch.stats.wisdom}\n"
             f"* Shadow Scars: {shadow_scars}\n"
             f"* Status: {status}")
    if prefix_desc:
        desc = f"{prefix_desc}\n\n{stats}"
    else:
        desc = stats
    return common_utils.embed_msg(title=title, desc=desc, footer=footer)


def validate_shadow_path(ch):
    """Validates shadow path exists and is properly formatted"""
    try:
        shadow_path = load_json(ch.get_cvar(SHADOW_PATH))
        if not all(key in shadow_path for key in ["calling", "path", "currentFlaws"]):
            return False, "Shadow path data is corrupted. Please run `!lotrshadow setup` to reinitialize."
        return True, None
    except:
        return False, "Shadow path data not found. Please run `!lotrshadow setup`."


def validate_shadow_source(source):
    """Validates source and amount for shadow resistance"""
    shadow_data = load_json(get_gvar(METADATA_SHADOW))

    if source not in shadow_data["shadowSources"]:
        return False, f"Invalid source. Must be one of: {', '.join(shadow_data['shadowSources'].keys())}", None

    return True, None, shadow_data["shadowSources"][source]


def get_flaws_until(path_flaws, target_flaw):
    """Gets list of flaws up to and including target flaw"""
    if not target_flaw:
        return []

    flaws = []
    for flaw in path_flaws:
        flaws.append(flaw)
        if flaw == target_flaw:
            break
    return flaws


def make_lotr_check_roll(character, check, adv=0, bonuses=None):
    """Makes a vroll for a LOTR or standard skill check.

    Args:
        character: Character making check
        check: Skill name (LOTR skill or standard skill)
        adv: Advantage state (-1 dis, 0 normal, 1 adv)
        bonuses: List of bonus strings to add to roll
    Returns:
        SimpleRollResult of the check roll
    Raises:
        ValueError: If skill is not found in LOTR skills or standard skills
    """
    # Load LOTR skill data
    skills_data = load_yaml(get_gvar(METADATA_CHECK))
    char_skills = load_yaml(character.get_cvar(LOTR_SKILLS, '{}'))

    # Build base advantage roll string
    roll_str = "2d20kh1" if adv == 1 else "2d20kl1" if adv == -1 else "1d20"

    # Case 1: LOTR skill
    if check in skills_data['skills']:
        skill_data = skills_data['skills'][check]
        ability = skill_data['ability']

        # Get base ability modifier
        roll_str += f"+{character.stats.get_mod(ability)}"

        # Add proficiency if character has it
        if check in char_skills:
            prof_level = char_skills[check]
            prof_mult, prof_name = common_utils.PROFICIENCY_LEVELS[prof_level]
            if prof_mult > 0:
                prof_bonus = floor(
                    character.stats.prof_bonus * prof_mult) if prof_mult == 0.5 else character.stats.prof_bonus * prof_mult
                roll_str += f'+{prof_bonus}["{prof_name}"]'

    # Case 2: Standard skill
    else:
        try:
            roll_str += f"+{character.skills[check]}"
        except:
            raise ValueError(f"Check {check} not found in LOTR skills or standard skills")

    # Add any additional bonuses
    if bonuses:
        roll_str += "+" + "+".join(bonuses)

    return vroll(roll_str)


def get_blessing_die(character):
    return BLESSING_DIE.get(character.stats.prof_bonus)
