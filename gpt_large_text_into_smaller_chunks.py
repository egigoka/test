from commands import OS, File, List, copy, paste

input_file = OS.args[1]

content = File.read(input_file)

output_file = input_file + ".smaller.txt"

CONTEXT_WINDOW = 4096

PROMPT_LENGTH_TOKENS = 200

TOKEN_MULTIPLIER_UNICODE = 1.5
TOKEN_MULTIPLIER_EN = 3.75

TOKEN_MULTIPLIER = TOKEN_MULTIPLIER_EN
if "u" in OS.args:
    TOKEN_MULTIPLIER = TOKEN_MULTIPLIER_UNICODE

CHUNKS = List.split_every(content, int(CONTEXT_WINDOW*TOKEN_MULTIPLIER-PROMPT_LENGTH_TOKENS))

File.wipe(output_file)

total = len(CHUNKS)
for cnt, chunk in enumerate(CHUNKS):
    chunk_cnt = cnt + 1
    print(f"{chunk_cnt} / {total} chunk request copied to clipboard, feed it into chatgpt")
    prompt = (f"Content: \"\"\"{chunk}\"\"\"\n"
            + f"It's chunk of data #{chunk_cnt} of {total} chunks total.\n\n"
            + "Please remove information that isn't valuable.\n\n"
            + "Only save the most valuable information that will be helpful.\n\n"
            + "Write all valuable information from this chunk of text.\n\n"
            + "Format it as code for easier copying, please.\n\n"
            + "Use markdown to emphasize information of the most importance. Thank you."
            )
    copy(prompt)

    print("press Enter when answer is in clipboard")
    input()
    output = paste()

    if prompt.strip() != output.strip():
        print("saved new info")
        File.write(output_file, f"<<<{chunk_cnt}>>>\n{output}\n\n", mode="a")
    else:
        print("no new info, skipping")

print(f"done, check file {output_file}")
