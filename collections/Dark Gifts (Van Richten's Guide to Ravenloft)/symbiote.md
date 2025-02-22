`!symbiote [show] [random] [-str #] [-dex #] [-con #] [-int #] [-wis #] [-cha #] [override|delete]`

## Description
Manages a character's symbiote, allowing users to create, modify, view, and delete a symbiotic bond that influences ability scores.

## Arguments
**Optional arguments**
  - `show` - Displays the current symbiote stats.
  - `random` - Generates a random set of ability scores for the symbiote.
  - `override` - Replaces an existing symbiote with new values.
  - `delete` - Removes the current symbiote.

_If manually set, all ability scores must be provided:_
  - `-str #` - Sets Strength to the given value.
  - `-dex #` - Sets Dexterity to the given value.
  - `-con #` - Sets Constitution to the given value.
  - `-int #` - Sets Intelligence to the given value.
  - `-wis #` - Sets Wisdom to the given value.
  - `-cha #` - Sets Charisma to the given value.

## Examples
Display the current symbiote stats:
```
!symbiote show
```
Generate a random symbiote:
```
!symbiote random
```
Set a symbiote manually:
```
!symbiote -str 14 -dex 12 -con 16 -int 10 -wis 8 -cha 15
```
Override an existing symbiote:
```
!symbiote override -str 13 -dex 11 -con 15 -int 9 -wis 7 -cha 14
```
Delete the symbiote:
```
!symbiote delete
```

## Notes
- All ability scores must be specified when manually setting a symbiote.
- If a symbiote already exists, the `override` argument must be used to replace it.
 
## Issues?
You can file reports and feature requests as well as see the source code on [**GitHub**](https://github.com/fatestapestry/avrae-collections).

## Support Me!
Please consider contributing to future development and maintenance by supporting me on [**Patreon**](https://www.patreon.com/fatestapestry), or donating on [**Ko-Fi**](https://ko-fi.com/noralf).
