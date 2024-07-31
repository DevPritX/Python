from text_to_speech import save

text = "Hello World!"
language = "en"
output_file = "hello_world_slow.mp3"

save(text, language, slow=True, file=output_file)