# JSTemplatify
JSTemplatify is a plugin for Sublime Text that converts the current selection to a JavaScript [template string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)

## Keybindings
- Convert current selection to JavaScript Template:  "ctrl+alt+j", "ctrl+alt+t"

## Example:
```javascript
// INPUT:
'hello ' + name

// OUTPUT:
`hello ${name}`
```

## Install
#### Package Control
Open the Command Palette, type ***`pci`*** to bring up **`Package Control: Install Package`**, hit Enter,
then search for `JSTemplatify`.

#### Git Clone
Clone this repository in to the Sublime Text "Packages" directory, which is located where ever the
"Preferences" -> "Browse Packages" option in Sublime takes you.

## Contributors
- Matt Rinker

## License
Copyright (C) 2020 Matt Rinker

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
