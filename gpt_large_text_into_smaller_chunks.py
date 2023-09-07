from commands import *

input_file = OS.args[1]

content = File.read(input_file)

output_file = input_file + ".smaller.txt"

chunks = List.split_every(content, int(4000*3.75-100))

File.wipe(output_file)

for cnt, chunk in enumerate(chunks):
    print("chunk copied to clipboard, feed it into chatgpt")
    copy(f"Please, remove some information not applicable to main topic of text that i'll send you in chunks. "
         + f"Only save most valuable information that will be helpful in solving problem. "
         + f"Save related practices and commands that can be helpful in solving problems. "
         + f"I'ts chunk #\"{cnt}\". "
         + f"Content of chunk: \"\"\"{chunk}\"\"\"")

    print("press Enter when output is in your clipboard")
    input()
    output = paste()

    File.write(output_file, output + newline)

print(f"done, check file {output_file}")
