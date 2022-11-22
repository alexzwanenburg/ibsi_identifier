import numpy as np
import string


def create_random_codes(k=1, start=0, n_digits=4):

    # Get list of upper-case letters and digits
    character_list = list(string.ascii_uppercase + string.digits)
    n_characters = len(character_list)

    # Get maximum number of combinations for n_digits
    n_max = n_characters**n_digits

    # Set seed for random number generator
    np.random.seed(37)

    # Draw k+start random numbers, without resampling
    all_int_codes = np.arange(start=0, stop=n_max-1, step=1, dtype=int)
    int_codes = np.random.choice(all_int_codes, size=k+start, replace=False)

    # Remove all before start so that k codes remain
    int_codes = int_codes[start:]

    # Decompose to get the index to the characters
    code_list = []
    remainder = int_codes
    for ii in np.arange(n_digits)[::-1]:
        quotient, remainder = np.divmod(remainder, n_characters**(ii))
        code_list.append(quotient)

    # Replace integer by characters. Every n_digits now forms one code
    code_list = np.array(character_list)[np.ravel(np.array(code_list), order="F")]
    code_list = np.split(code_list, indices_or_sections=k, axis=0)

    # Concatenate to strings
    code_list = [''.join(row) for row in code_list]

    return code_list


def save_list(code_list, file_path):

    file = open(file=file_path ,mode="w")
    file.writelines( "%s\n" % item for item in code_list)

    file.close()


identifier_list = create_random_codes(k=200, start=413)
save_list(code_list=identifier_list, file_path="ibsi_codes.txt")
