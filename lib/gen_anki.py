import genanki

my_model = genanki.Model(
  1607392319,
  'Simple Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ])

def generate_anki_deck(list_of_texts, season, episode):
  my_deck = genanki.Deck(
    2059400110,
    f"Better Call Saul {season} {episode}")
  
  for eng_and_pt in list_of_texts:
    my_note = genanki.Note(
      model=my_model,
      fields=eng_and_pt)

    my_deck.add_note(my_note)
  genanki.Package(my_deck).write_to_file(f"/root/main/output/Better Call Saul {season} {episode}.apkg")
  