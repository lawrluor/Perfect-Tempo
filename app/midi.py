'''
import mido

msg = mido.Message('note_on', note=60)
msg.type
msg.note
msg.bytes()
msg.copy(channel=2)

# port = mido.open_output('Port Name')
port = mido.open_output(name='foo', virtual=True)
port.send(msg)

with mido.open_input() as inport:
  for msg in inport:
    print(msg)
'''

import mido

from mido import MidiFile
output = mido.open_output(name='foo', virtual=True)

for message in MidiFile('test.mid').play():
  output.send(message)
