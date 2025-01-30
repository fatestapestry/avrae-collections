`!anguished [-t target]`

## Description
Applies the "Anguished" effect to one or more targets in combat. This effect imposes penalties and provides a button to remove it when needed.

## Arguments

**Optional arguments:**
- `-t <target>` - Specifies one or more combatants to receive the effect. Defaults to the active character if not provided.

## Examples
```plaintext
!anguished
```
Applies the "Anguished" effect to the active character.

```plaintext
!anguished -t Aragon
```
Applies the "Anguished" effect to Aragon.

```plaintext
!anguished -t Legolas -t Gimli
```
Applies the "Anguished" effect to both Legolas and Gimli.

## Notes
- The effect can only be applied to combatants currently in combat.
- If the target already has the "Anguished" effect, it will not be added again.
- The effect includes a button to remove it manually.

## Issues?
You can file reports and feature requests, as well as see the source code, 
at my [GitHub](https://github.com/fatestapestry/avrae-collections)

## Support Me
You can support me and future development at [Ko-Fi](https://ko-fi.com/noralf)
