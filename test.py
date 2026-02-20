#!/usr/bin/env python3
import sys
import os
import genanki
import random

# TODO Handle duplicate media file names (e.g. if I have two different videos both named "clip.mp4", how do I add them both to the same collection.media folder without overwriting one of them?)

random_video_info = str(random.randrange(1 << 30, 1 << 31))
path_to_video = "/Users/grace/tmp/"
original_video_filename = "lazy_av1_again.mp4"
video_filename = "lazy_av1_again_" + random_video_info + ".mp4"
output_file = "awesome_lazy_output_file_" + random_video_info


os.system("cp " + path_to_video + original_video_filename + " " + path_to_video + video_filename) 

# Define the model (any note type)
random_model_id = random.randrange(1 << 30, 1 << 31)
model = genanki.Model(
    model_id=random_model_id ,
    name='Video Style' + str(random_model_id),
    fields=[
        {'name': 'Front'},
        {'name': 'VideoFileName'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': "{{Front}}",
            'afmt': """<video width="600" controls autoplay>

<source src="{{VideoFileName}}" type="video/mp4">

Your browser does not support the video tag.

</video>""" ,
        }
    ]
)

# Create a note with video on the front, word on back
note = genanki.Note(
    model=model,
    fields=['short_video', video_filename]
)

random_deck_id = random.randrange(1 << 30, 1 << 31)

# Create a deck
deck = genanki.Deck(
    deck_id=random_deck_id,
    name='Video Deck_' + str(random_deck_id)
)
deck.add_note(note)

# Create a package with the image file
package = genanki.Package(deck)

package.media_files = [path_to_video + video_filename]

# Write to output file
output_path = os.path.join(os.path.dirname(__file__) + "/apkgs/", output_file + '.apkg')
package.write_to_file(output_path)

# TODO automate this or something. 
# write to collections.media
# for file in package.media_files:
#     os.system("cp " + file + "collections.media/" + os.path.basename(file))

print(random_model_id)
print(random_deck_id)
print(f"✓ Flashcard created: {output_path}")
