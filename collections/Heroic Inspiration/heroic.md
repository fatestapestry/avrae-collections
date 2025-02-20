`!heroic [-die <str> add|del]`

## Description
This alias allows you to manage the use of Heroic Inspiration for characters. It can be used to roll for Heroic Inspiration or modify its counter. If the counter does not exist, it will be created.

## Arguments
**Positional arguments**
- None required.

**Optional arguments**
- `-die <str>` - The die to roll when using Heroic Inspiration. Defaults to `1d20`.
- `add` - Adds a point of Heroic Inspiration.
- `del` - Removes a point of Heroic Inspiration.

## Examples
```
!heroic
```
Rolls a `1d20` for Heroic Inspiration.

```
!heroic -die 1d10
```
Rolls a `1d10` for Heroic Inspiration.

```
!heroic add
```
Adds a point of Heroic Inspiration to the counter.

```
!heroic del
```
Removes a point of Heroic Inspiration from the counter.

## Notes
- A counter for Heroic Inspiration is automatically created if it doesn't exist.
- Using `add` or `del` does not roll a die, only modifies the Heroic Inspiration counter.

## Issues?
You can file reports and feature requests as well as see the source code on [**GitHub**](https://github.com/fatestapestry/avrae-collections)

## Support Me!
Please consider contributing to future development and maintenance by supporting me on [**Patreon**](https://www.patreon.com/fatestapestry), or donating on [**Ko-Fi**](https://ko-fi.com/noralf).
