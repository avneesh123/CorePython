from pprint import pprint as pp


def tuple_learn():
    first = (1,)
    print(type(first))
    second = 1, 2, 3, 4, 5
    print(second)
    (a, (b, c, (d, e))) = (1, (2, 3, (4, 5)))  # nested destructing
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    a = 'jelly'
    b = 'bean'
    a, b = b, a  # swapping packing and unpacking a tuple happening here
    print(a + b)

    # creating tuple from existing object using tuple constructor
    create_from_existing = tuple([561, 1105, 1345, 5343])
    # check for containment using in operator
    print(561 in create_from_existing)
    print(561 not in create_from_existing)


def min_max(items):
    return min(items), max(items)  # returning tuple


def demo_enumerator():
    list_demo = [6, 354, 64545, 454, 4546, 3242342]
    for p in enumerate(list_demo):
        print(p)
    for i, v in enumerate(list_demo):
        print(f"i = {i}, v = {v}")


def demo_list():
    list_demo = [23, 343, 34355, 454, 454554, 223, 666454, 435453]
    print(f" Copies 2nd and 3rd element list_demo[1:3] = {list_demo[1:3]}")
    print(f" Copies all element from 3rd element list_demo[2:] = {list_demo[2:]}")
    print(f" Copies first two elements list_demo[:2] = {list_demo[: 2]}")
    copy_list_demo = list_demo[:]
    print(f" Copied list list_demo[:] = {copy_list_demo}")
    print(f" list_demo and copy_list_demo are distinct list copy_list_demo is list_demo= {copy_list_demo is list_demo}")
    print(
        f" Since copy_list_demo is a copy it has a same value copy_list_demo == list_demo= {copy_list_demo == list_demo}")
    # Remember we have 2 different list objects but elements within it are references to same obj refer to by the
    # original list
    print(f" other way to copy list_demo.copy() = {list_demo.copy()}")
    print(f" other way to copy [Preferred as can be applied for other collections] list(list_demo) = {list(list_demo)}")
    # all above approach do a shallow
    a = [[1, 2], [3, 4]]
    b = a[:]
    print(f"shallow copy - a is b  = {a is b}")
    print(f"shallow copy - a == b  = {a == b}")
    print(f"shallow copy - a[0] is b[0] = {a[0] is b[0]}")
    print(f"shallow copy - a[1].append(5)= {a[1].append(5)}")
    print(f"shallow copy - b[1]= {b[1]}")
    # initializing list with constant size with default value
    print(f"initializing list with constant size with default value [0]*9 = {[0] * 9}")
    # repetition will have reference to same value
    repetition = [[1, 2]] * 5
    repetition[1].append(7)
    print(f"repetition has reference - {repetition}")
    w = "the quick brown fox jumps over the the the".split()
    print(f"index method -- - {w.index('fox')}")
    # print(f"index method value error if not found -- - {w.index('unicorn')}")
    print(f"count method -- - {w.count('the')}")
    print(f"in and not in works the same way -- - {'the' in w}")
    # remove using a del and remove method
    u = "jackdaws love my big sphinx of quartz".split()
    print(u)
    print(f"remove method in list uses the value to remove and give value error if not found but delete del u[3] uses "
          f"index -- - {u.remove('quartz')}")
    print(u)

    # insert method
    a = "I love universe mysteries a lot".split()
    print(a)
    a.insert(6, "agreed")
    print(f"''.join(a) == {' '.join(a)}")

    # Concatenating list
    m = [2, 1, 3]
    n = [4, 7, 11]
    k = m + n
    print(f"concatenating with + operator creates new without modifying the existing k = m+n == {k}")
    print(f"appending to previous list = m.append(5)  = {m.append(5)} == {m}")
    print(f"printing k again = {k}")
    k += [100, 101]
    print(f"Augment operator modify the assignee in place k += [100, 101] == {k}")
    k.extend([-999])
    print(f"extend works the same way k.extend([-999]) == {k}")

    # list rearrangement in place
    g = [1, 11, 21]
    g.reverse()
    print(f"reverse works in place = {g}")
    h = [17, 41, 29]
    h.sort(reverse=True)
    print(f"sort method accept two optional param key and reverse [if true sort in desc] h.sort(reverse=true)= {h}")
    i = 'not perplexing do handwriting family get out nice movie wassip how you doing !!'.split()
    i.sort(key=len)
    print(f"sort method key param accepts any callable obj which is then used to extract a key from each item   "
          f"i.sort(key=len) = {i}")
    # list rearrangement out of place means new list is done using reversed() and sorted()
    # they return a reverse iterator and a new list, respectively
    j = [4, 9, 2, 1]
    k = sorted(j)
    print(f" sorted gives new list  k = sorted(j) == {k}")

    reversed_demo = [9, 3, 1, 0]
    reversed_iterator = reversed(reversed_demo)
    reversed_list = list(reversed_iterator)
    print(f" reversed gives an obj of type list reverse iterator we can pass this to list constructor to creat an "
          f"actual list == {reversed_list}")


def demo_dictionaries():
    # keys must be immutable so list can't be used as a key
    # Don't rely on order of items in dict
    dict_line = ''.join(['*'] * 200)
    print(dict_line)
    print('Dictionary starts here')
    print(dict_line)
    dict_first = {'google': 'https://google.com',
                  'yahoo': 'https://yahoo.com'}
    names_and_ages = [('Alice', 32), ('Bob', 34), ('Charlie', 28)]
    dict_names_and_ages = dict(names_and_ages)
    print(
        f"just like others we have dict constructor to convert from other type to dict tupe to dict == {dict_names_and_ages}")
    dict_directly = dict(a='alpha', b='bravo', c='charlie', d='delta')
    print(f"create dic directly by passing key value to dict constructor == {dict_directly}")
    # as with list dict copying is also shallow
    print(f"either use the copy method == {dict_names_and_ages.copy()}")
    print(f"or directly pass the to the constructor == {dict(dict_names_and_ages)}")
    dict_directly.update(dict_first)
    print(f"merge dict using update method == dict_directly.update(dict_first) {dict_directly}")

    # loop over dict return keys
    for site in dict_first:
        print(f"key site -  {site} and value url is - {dict_first[site]}")

    # to iterate oer values
    for url in dict_first.values():
        print(f"using values() method to get just values value url is - {url}")

    # to get key and value at one go as tuple using items() method
    for key, value in dict_first.items():
        print(f" Using items method to get  key and value together {key} ==> {value}")

    print(f"use in to check if keys are part of dict - 'google' in dict_first = {'google' in dict_first}")

    # dict initialize can be over multiple lines

    isotopes = {
        'H': [1, 2, 3],
        'He': [3, 4],
        'Li': [6, 7],
        'Be': [7, 9, 10]
    }

    isotopes['H'] += [111, 343, 3434, 3435435]
    print(f"appending using augment operator = {isotopes}")
    print("using pretty print to print better")
    pp(isotopes)


def demo_set():
    # unordered collection of unique element
    # sets are mutable
    # elements in set must be immutable

    first_set = {3, 5, 6, 61}
    print(first_set)
    print(type(first_set))
    print("since empty curly braces create new dict to create new set we need to use set()")
    empty_set = set()
    set_from_list = set([1, 3, 5, 5, 3, 33])
    print(f"you can create set from list and duplicate will be discarded == {set_from_list}")
    set_from_list.add(44)
    print(f"for adding an element use the add() method == {set_from_list}")
    set_from_list.update([37, 45, 5545, 3454325, 233432])
    print(f"for adding multiple elements use the update() method == {set_from_list}")
    # set algebra relationship
    blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia'}
    blond_hairs = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
    smell_hcn = {'Harry', 'Amelia'}
    taste_ptc = {'Harry', 'Lily', 'Amelia', 'Lola'}
    o_blood = {'Mia', 'Joshua', 'Lily', 'Olivia'}
    b_blood = {'Jack', 'Amelia'}
    a_blood = {'Harry'}
    ab_blood = {'Joshua', 'Lola'}

    print(f"Blue eyes or blond hair union using blue_eyes.union(blond_hairs) = {blue_eyes.union(blond_hairs)}")
    print(f"Blue eyes and blond hair union "
          f"using blue_eyes.intersection(blond_hairs) = {blue_eyes.intersection(blond_hairs)}")
    print(
        f"Blond hair and no Blue eyes using difference method"
        f" blue_eyes.difference(blond_hairs) = {blond_hairs.difference(blue_eyes)}")
    print(
        f"Get people having Blond hair OR Blue eyes but not both using symmetric_difference method"
        f" blue_eyes.symmetric_difference(blond_hairs) = {blond_hairs.symmetric_difference(blue_eyes)}")
    print(f"Check if set is subset of other  use smell_hcn.issubset(blond_hairs) = {smell_hcn.issubset(blond_hairs)}")
    print(f"to check reverse of above use taste_ptc.issuperset(smell_hcn) = {taste_ptc.issuperset(smell_hcn)}")
    print(f"to check if two sets have no element in common use a_blood.isdisjoint(b_blood) = {a_blood.isdisjoint(b_blood)}")


if __name__ == '__main__':
    tuple_learn()
    print(min_max([43, 3, 54, 66, 454, 45454522, 213]))
    lower, upper = min_max([43, 3, 54, 66, 454, 45454522, 213])  # Destructing
    print(lower)
    print(upper)
    demo_enumerator()
    demo_list()
    demo_dictionaries()
    demo_set()
