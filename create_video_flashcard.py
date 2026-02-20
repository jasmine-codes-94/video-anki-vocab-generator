#!/usr/bin/env python3
import sys
import os


"""
Successfully moved clip to collection.media 

"""

# Import genanki from the local recurse/genanki directory
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'genanki'))
import genanki

# Define the model (any note type)
model = genanki.Model(
    model_id=1234567811,
    name='Flower Study',
    fields=[
        {'name': 'Back'},
        {'name': 'VideoFileName'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': """<video width="600" controls autoplay>

<source src="{{VideoFileName}}" type="video/mp4">

Your browser does not support the video tag.

</video>""",
            'afmt': '{{Back}}',
        }
    ]
)

# Create a note with Chinese character on front, image on back
note = genanki.Note(
    model=model,
    fields=['short_video', 'awesome.mp4']
)

# Create a deck
deck = genanki.Deck(
    deck_id=2333400144,
    name='awesome video deck'
)
deck.add_note(note)

# Create a package with the image file
package = genanki.Package(deck)
package.media_files = ['/Users/grace/Documents/recurse/chinese_videos/pronunciation/awesome.mp4']

# Write to output file
output_path = os.path.join(os.path.dirname(__file__), 'awesome.apkg')
package.write_to_file(output_path)

print(f"✓ Flashcard created: {output_path}")
