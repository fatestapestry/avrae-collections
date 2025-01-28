`!lotrevent <role> <event> [args]`

## Description
Facilitates a LOTR-themed journey event resolution by performing a skill check based on the specified role and event type. Supports various modifiers and conditions to customize the event outcome.

## Arguments

Positional arguments:
- `<role>` - `[scout, lookout, hunter]`. Specifies the journey role for the character. Must be one of the valid roles defined in the system.
- `<event>` - `[terriblemisfortune|tm, despair|dp, illchoices|ic, mishap|mh, shortcut|sc, chancemeeting|cm, joyfulsight|js]`. Specifies event type. Supports abbreviations.

Optional arguments:
- `adv|dis` - Specifies advantage or disadvantage on the event roll.
- `autumn|winter` - Overrides `adv|dis` to disadvantage on the skill check due to seasonal conditions.
- `-terrain <value>` - `[hardterrain, openterrain, roads]`. Defaults to `openterrain` (DC 15).
- `-dc <value>` - Overrides the default difficulty class (DC) for the terrain.
- `-b <bonus>` - Adds a custom bonus to the skill check roll.
- `multipleroles` - Applies a `-5` penalty for taking multiple roles during the journey.
- `blessingdie` - Adds a blessing die to the skill check roll.

## Examples
```plaintext
!lotrevent scout terriblemisfortune
```
Performs a `Scout` skill check for the `Terrible Misfortune` event on open terrain.

```plaintext
!lotrevent hunter cm -terrain hardterrain adv blessingdie
```
Performs a `Hunter` skill check for the `Chance Meeting` event on hard terrain with advantage and a blessing die.

```plaintext
!lotrevent lookout despair -dc 20 dis -b 2
```
Performs a `Lookout` skill check for the `Despair` event with a DC of 20, disadvantage, and a +2 bonus.

## Issues?
You can file reports and feature requests, as well as see the source code, 
at my [GitHub](https://github.com/fatestapestry/avrae-collections)

## Support Me
You can support me and future development at [Ko-Fi](https://ko-fi.com/noralf)
