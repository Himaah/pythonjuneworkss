# email_id="gouri@gmail.com"

# at_index=email_id.index("@")

# username=email_id[:at_index]
# print(username)

# domain=email_id[at_index:]
# print(domain)


# anagram

source_word="listen"
target_word="silent"

sorted_source=sorted(source_word)
sorted_target=sorted(target_word)

print(sorted_source==sorted_target)



# defining anagram

def isAnagram(word1,word2):
    return sorted(word1)==sorted(word2)

sourcee="listen"
targett="silent"

print(isAnagram(sourcee,targett))

def isKangaroo(word1,word2):
