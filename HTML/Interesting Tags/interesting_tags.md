# Interesting HTML Tags

## abbr
```html
<p>This is an abbreviation
    <abbr title="Three Letter Acronym">TLA</abbr>
</p>
```
Renders as (hover over abbr):
<p>This is an abbreviation
    <abbr title="Three Letter Acronym">TLA</abbr>
</p>

<br>

# bdo
bdo lets you specify text direction:
```html
<p>
    <bdo dir="rtl"> <!-- RightToLeft-->
    Left to right text
</p>
```
Renders as:
<p>
    <bdo dir="rtl"> <!-- RightToLeft-->
    Left to right text
</p>

<br>

# kbd
kbd denotes a key of the keyboard:
```html
<p>
    Press <kbd>Ctrl</kbd> + <kbd>+</kbd> for zoom in.
</p>
```
Renders as:
<p>
    Press <kbd>Ctrl</kbd> + <kbd>+</kbd> for zoom in.
</p>

<br>

# samp
With samp you get a computer output like style:
```html
<p>
    <samp>I am a computer</samp>
</p>
```
Renders as:
<p>
    <samp>I am a computer</samp>
</p>

<br>

# details and summary
Self explanatory:
```html
<details>
    <summary>
        Title #1
    </summary>
    Content #1
</details>
<details>
    <summary>
        Title #2
    </summary>
    Content #2
</details>
```
Renders as:
<details>
    <summary>
        Title #1
    </summary>
    Content #1
</details>
<details>
    <summary>
        Title #2
    </summary>
    Content #2
</details>

<br>

# input types
``` html
<input type="color">
```
Renders as:
<input type="color">

``` html
<input type="range" value="2" min="1" max="5">
```
Renders as:
<input type="range" value="2" min="1" max="5">

``` html
<input type="datetime-local"> <!-- or date, datetime, time, week -->
```
Renders as:
<input type="datetime-local">

<br>

# meter
``` html
<meter max="100" min="1" value="60"></meter>
```
Renders as:
<meter max="100" min="1" value="60"></meter>

<br>

# progress
``` html
<progress></progress>
```
Renders as:
<progress></progress>

<br>

# datalist
``` html
<input type="text" list="suggestions" placeholder="fruits">
<datalist id="suggestions">
    <option>Banana</option>
    <option>Orange</option>
    <option>Kiwi</option>
    <option>Apple</option>
</datalist>
```
Renders as:
<input type="text" list="suggestions" placeholder="fruits">
<datalist id="suggestions">
    <option>Banana</option>
    <option>Orange</option>
    <option>Kiwi</option>
    <option>Apple</option>
</datalist>

<br>

# optgroup
``` html
<select>
    <optgroup label="Fruits">
        <option>Banana</option>
        <option>Tangerine</option>
    </optgroup>
    <optgroup label="Vegetables">
        <option>Lettuce</option>
        <option>Spinach</option>
    </optgroup>
</select>
```
Renders as:
<select>
    <optgroup label="Fruits">
        <option>Banana</option>
        <option>Tangerine</option>
    </optgroup>
    <optgroup label="Vegetables">
        <option>Lettuce</option>
        <option>Spinach</option>
    </optgroup>
</select>
