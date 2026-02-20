Minimal Anki add-on: create one test flashcard


https://juliensobczak.com/write/2016/12/26/anki-scripting/

Install (macOS example):

1. Copy the folder `anki_simple_create_card` into your Anki add-ons directory. For Anki 2.1 on macOS this is typically:

```bash
cp -R anki_simple_create_card ~/Library/Application\ Support/Anki2/addons21/
```

2. Restart Anki.
3. In Anki, open Tools -> Create test card (or press Ctrl+Shift+T). A single note with Front/Back fields will be added to the `Default` deck.

Notes:
- You can change the deck by editing `did = mw.col.decks.id("Default")` in `__init__.py`.





-----------

Julian Sobczak 


Collection  table
    - Deck(s)
    - models (aka Note Types) 
    - Tags

Cards table
    - due (when card should appear again)

Notes table
    - did (deck override. id?)
    - contains the *actual* card info like 水：water.
    - 1 Note may link to multiple cards (think of how you can fill out 1 Add in the and generate both the input and the reversed input as cards)

Revlog table
    - where reviews are registered 