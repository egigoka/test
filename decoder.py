from commands import *
# data
bad_string = CLI.multiline_input("bad string ")
good_string = input("good string ")
# debug flags
print_errors = False
pause_after_each_success = False
print_same_results = False


def decode(bad_string, good_string):
    possible_outputs = []
    cnt = 0
    for enc_in in Str.python_encodings:
        for enc_out in Str.python_encodings:
            try:
                # trying to re-encode string
                bytes_ = bad_string.encode(encoding=enc_in)
                decoded_string = bytes_.decode(encoding=enc_out)

                # print string if requirements are met
                if good_string in decoded_string:

                    if decoded_string not in possible_outputs or print_same_results:
                        print(f"'{decoded_string[:200]}' [{enc_in} > {enc_out}]")

                    # update possible_outputs
                    if decoded_string not in possible_outputs:
                        possible_outputs.append(decoded_string)

                    cnt += 1
                if pause_after_each_success:
                    input("press Enter to continue")
            except Exception as e:
                if print_errors:
                    print(f"{e} [{enc_in} > {enc_out}]")

    print()
    print("total without errors", cnt)
    print("different outputs", len(possible_outputs))


if __name__ == '__main__':
    decode(bad_string, good_string)
    input("Enter to exit")