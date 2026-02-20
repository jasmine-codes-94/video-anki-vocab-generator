#!/usr/bin/env python3
import sys
import os

# Import genanki from the local recurse/genanki directory
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'genanki'))
import genanki

# Define the model (any note type)
model = genanki.Model(
    model_id=1234567888,
    name='screen Study',
    fields=[
        {'name': 'Front'},
        {'name': 'Back'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Front}}',
            'afmt': '{{Back}}',
        }
    ]
)

# Create a note with Chinese character on front, image on back
note = genanki.Note(
    model=model,
    fields=['screen', '<img src="screen.png">']
)

# Create a deck
deck = genanki.Deck(
    deck_id=2059400188,
    name='Chinese screens'
)
deck.add_note(note)

# Create a package with the image file
package = genanki.Package(deck)
package.media_files = ['/Users/grace/Documents/recurse/media/screen.png']

# Write to output file
output_path = os.path.join(os.path.dirname(__file__), 'screen_flashcard.apkg')
package.write_to_file(output_path)

print(f"✓ Flashcard created: {output_path}")
