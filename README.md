# dash-wrapper
A wrapper around dash that allows a new syntax to define the layout of your app.

The idea is of this package is to simplify the syntax for nesting `html`  elements in your app layout.
When you want to import an element, instead of:

```
import dash_core_components as dcc
import dash_html_components as html

element1 = html.Div()
element2 = dcc.Input()
```

you would simply do:

```
from dash_wrapper import dash_core_components as dcc
from dash_wrapper import dash_html_components as html

element1 = html.Div()
element2 = dcc.Input()
```

And you are good to go. Your elements now have additional functionality that I will explain below.

In the following examples notice that, since this API implements the nesting of elements as a single chain of arithmetic operations, you need to either wrap everything inside parenthesis or you can use the backslash `\` at the end of each line. Even though this is not required (you could do a very long one liner if you want) of course it is strongly suggested to use it in order to visualize the structure of the layout.
(IMHO the benefit becomes obvious after you add a few elements the layout).

There are 5 simple rules to define the layout :
1. **add an element on the lower level with `*`**
2. **add an element on the same level with `@`**
3. **add an element on the previous level with `/`**
4. **add an element on the nth previous level with `/n/`**
5. **add an element on A specific level with `%n%`**

**Example 1: add an element on the lower level with `*` AKA add a child**

standard API:
```
Div(Div(id='level1-child1'), id='level0-parent')
```
new API:
```
(
Div(id='level0-parent') *     # level 0 (with * we specify to add the next element to level 1, i.e. to the children of level 0)
    Div(id='level1-child1')   # level 1 
)
```

**Example 2: add an element on the same level with `@` AKA add a sibling**

standard API:
```
Div([Div(id='level1-child1'), 
     Div(id='level1-child2')], 
id='level0-parent')
```
new API:

```
(
Div(id='level0-parent') *       # level 0 (with * we specify to add the next element to level 1, i.e. to the children of level 0)
    Div(id='level1-child1') @   # level 1 (with @ we specify to add the next element to level 1, i.e. same level)
    Div(id='level1-child2')     # level 1
)
```

**Example 3: add an element on the previous level with `/` AKA add an uncle** 

standard API:
```
Div([
    Div(id='level1-child1'), 
    Div(
        Div(id='level2-child1'), 
    id='level1-child2'), 
    Div(id='level2-child1')], 
id='level0-level0-parent')
```
new API:

```
(
Div(id='level0-parent') *           # level 0 (with * we specify to add the next element to level 1, i.e. to the children of level 0)
    Div(id='level1-child1') @       # level 1 (with @ we specify to add the next element to level 1, i.e. same level)
    Div(id='level1-child2') *       # level 1 (with * we specify to add the next element to level 2, i.e. to the children of level 1)
        Div(id='level2-child1') /   # level 2 (with / we specify to add the next element to level 1 because we go back 1 level)
    Div(id='level1-child2')         # level 1
)
```

**Example 4: add an element on the nth previous level with `/n/` AKA add a nth-cestor**
This simply mean that you go back n levels

standard API:
```
Div([
    Div(id='level1-child1'), 
    Div(
        Div(
            Div(id='level3-child1'), 
        id='level2-child1'), 
    id='level1-child2'), 
    Div(id='level1-child3')], 
id='level0-parent')
```
new API:

```
(
Div(id='level0-parent') *                 # level 0 (with * we specify to add the next element to level 1, i.e. to the children of level 0)
    Div(id='level1-child1') @             # level 1 (with @ we specify to add the next element to level 1, i.e. same level)
    Div(id='level1-child2') *             # level 1 (with * we specify to add the next element to level 2, i.e. to the children of level 1)
        Div(id='level2-child1') *         # level 2 (with * we specify to add the next element to level 3, i.e. to the children of level 2)
            Div(id='level3-child1') /2/   # level 3 (with /2/ we specify to add the next element to level 1 because we go back 2 levels)
    Div(id='level1-child3')               # level 1
)
```

**Example 5: add an element on specific levev with `%n%`**
This is same of Example 4 but to specify the level we simply count forrward instead of countinc backward

new API:

```
(
Div(id='level0-parent') *                # level 0 (with * we specify to add the next element to level 1, i.e. to the children of level 0)
    Div(id='level1-child1') @            # level 1 (with @ we specify to add the next element to level 1, i.e. same level)
    Div(id='level1-child2') *            # level 1 (with * we specify to add the next element to level 2, i.e. to the children of level 1)
        Div(id='level2-child1') *        # level 2 (with * we specify to add the next element to level 3, i.e. to the children of level 2)
            Div(id='SubSubChild1') %1%   # level 3 (with %1% I specify to add the next element to level 1)
    Div(id='level1-child3')              # level 1
)
```

It should be clear that after a few divs the standard way of defining the layout becomes very messy to inspect and maintain. Especially if you want to move one element to another location you need to be careful with the parenthesis and which becomes tedious.

The way this is implemented implemented you just need to remember the **5 simple rules** for nesting elements.


