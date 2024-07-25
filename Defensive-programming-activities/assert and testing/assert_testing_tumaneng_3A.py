#CSEC 311 - DEFENSIVE PROGRAMMING - AY2023-24
#Assert and Testing - Activity
#marc_chrstian_tumaneng_BSCS_3A

def find_longest_word(sentences):# Define a set of common words to be excluded
    common_words = {"the", "and", "or", "over", "is", "are", "in", "on", "to"}

    longest_words = []# Initialize variables to keep track of the longest words
    max_length = 0

    for sentence in sentences:# Loop through each sentence
        words = sentence.split()# Split the sentence into individual words
        for word in words:# Examine each word in the sentence
            if word.lower() not in common_words and len(word) >= 4:# Skip commonly used words and those with a length less than 4
                if len(word) > max_length:# Update if the current word is longer than the current longest word
                    max_length = len(word)# Reset the list with the new longest word
                    longest_words = [word]
                elif len(word) == max_length:# If the word has the same length as the current longest word, add it to the list
                    longest_words.append(word)

    return longest_words  # Provide the list of longest words as the result


#pytest -v assert_testing_tumaneng_3A.py
#pytest test_assert_testing_tumaneng_3A.py