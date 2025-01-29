`!reinforced [-t target1]`

## Description
The `!reinforced` command grants a shield reinforcement effect to one or more combatants, increasing their AC by **+1**. This effect can only be applied to targets currently in combat.

## Arguments
- **Optional arguments:**
  - `-t <target>` - Specifies combatants to receive the Reinforced Shield effect. Defaults to the user if no targets are provided.

## Examples
```markdown
!reinforced
# Grants the Reinforced Shield effect to yourself

!reinforced -t Aragorn
# Grants the Reinforced Shield effect to Aragorn in combat

!reinforced -t Legolas -t Gimli
# Grants the Reinforced Shield effect to Legolas and Gimli in combat
```

## Notes
- This effect grants **+1 AC** while active.
- The effect can only be applied to targets in combat.
- A combatant cannot receive this effect more than once.
- The effect adds a button that allows the target to **remove** the Reinforced Shield bonus.
- Multiple targets supported.

## Issues?
You can file reports and feature requests, as well as see the source code, 
at my [GitHub](https://github.com/fatestapestry/avrae-collections)

## Support Me
You can support me and future development at [Ko-Fi](https://ko-fi.com/noralf)
