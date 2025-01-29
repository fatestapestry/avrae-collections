`!cunningmake [-t target]`

## Description
The `!cunningmake` command grants a Cunning-make enhancement to one or more combatants' armor, making it lighter and improving their ability to avoid fatigue. This effect increases their **AC by +1** while active.

## Arguments
- **Optional arguments:**
  - `-t <target>` - Specifies one or more combatants to receive the Cunning-make effect. Defaults to the user if no targets are provided.

## Examples
```markdown
!cunningmake
# Grants the Cunning-make effect to yourself

!cunningmake -t Boromir
# Grants the Cunning-make effect to Boromir in combat

!cunningmake -t Frodo -t Sam
# Grants the Cunning-make effect to Frodo and Sam in combat
```
1
## Notes
- This effect grants **+1 AC** while active.
- The effect can only be applied to targets in combat.
- A combatant cannot receive this effect more than once.
- The effect adds a button that allows the target to **remove** the Cunning-make bonus.
- Multiple targets can be specified in a single command.

## Issues?
You can file reports and feature requests, as well as see the source code,
at my [GitHub](https://github.com/fatestapestry/avrae-collections)

## Support Me
You can support me and future development at [Ko-Fi](https://ko-fi.com/noralf)

