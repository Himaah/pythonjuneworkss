#re.py
# to match patterns
# finditer(),search(),
# for identifying pattern finditer() is used.
# ===========================================================================

# finditer()

# parameters : pattern, variable name
# return as group of objects
# start and group

# ==========================================================================


# find python patterns and find count.

from re import finditer

text="hellopythonhellopythonhellopython"

python_matcher=finditer("python",text)
count=0
for m in python_matcher:
    print(m.start(),"===",m.group())

    count+=1
print("total count",count)
