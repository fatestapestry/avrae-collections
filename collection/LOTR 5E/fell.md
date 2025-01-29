`!fell <weapon> [-t target]`

## Description
The `!fell` command enhances a weapon attack with the *Fell* property, dealing additional damage on a critical hit. This command applies extra weapon dice to a critical hit and can target multiple combatants if specified.

## Arguments
**Positional arguments:**
  - `<weapon>` - The name of the base weapon being used in the critical hit. e.g. `shortsword`, `"light crossbow"`, etc.
**Optional arguments:**
  - `-t <target>` - Specifies one or more targets in combat to apply the damage to.

## Examples
```markdown
!fell longsword
# Applies the Fell property to a critical hit with a longsword

!fell warhammer -t Goblin1 -t Goblin2
# Applies the Fell property to a critical hit with a warhammer, rolling damage for Goblin1 and Goblin2
```

## Notes
- The Fell property increases critical damage by rolling **two additional weapon damage dice**.
- The weapon must be a standard weapon from the predefined list.
- If used in combat (`!i` system), the alias will apply damage directly to valid targets.
- If used outside combat, it will roll damage normally.
- This cannot be applied to a weapon with the **ammunition** property, but it can be applied to a single piece of ammunition instead.

## Issues?
You can file reports and feature requests, as well as see the source code,
at my [GitHub](https://github.com/fatestapestry/avrae-collections)

## Support Me
You can support me and future development at [Ko-Fi](https://ko-fi.com/noralf)

