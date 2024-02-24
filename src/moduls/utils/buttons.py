from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def keymakers(list_text:str, list_postdata:str, add_basics:bool=False):
    """**Function Description:**

The `keymakers` function creates an `InlineKeyboardMarkup` object from two lists: one with the text of the buttons and another with the data that will be sent when they are clicked. It also takes a boolean value indicating whether basic buttons (such as a back button) should be added.

**Parameters:**

* `list_text`: A list with the button text.
* `list_postdata`: A list with the data that will be sent when clicking the buttons.
* `add_basics` (optional): A boolean value indicating whether to add basic buttons. The default value is `False`.

**Return value:**

An `InlineKeyboardMarkup` object with the list of buttons.

**Example:**

```python
list_text = ["Button 1", "Button 2"]
list_postdata = ["data1", "data2"]

markup = keymakers(list_text, list_postdata)
```

The code above will create an `InlineKeyboardMarkup` object with two buttons:

* Button 1: Send the data "data1" as callback data.
* Button 2: Send the data "data2" as callback data."""

    lB = []
    buttons = []
    for text, postdata in zip(list_text, list_postdata):
        if postdata.startswith("WEB"):
            url = "-".join(postdata.split("-")[1:])
            lB += [InlineKeyboardButton(str(text), url=url)]
        else:
            lB += [InlineKeyboardButton(str(text), callback_data=postdata)]


    if add_basics:
        buttons = InlineKeyboardMarkup([lB, [InlineKeyboardButton(str(text), callback_data=str(postdata)) for text, postdata in zip(["Return"], ["start-0"])]])
    else:
        buttons = InlineKeyboardMarkup([lB])

    return buttons
