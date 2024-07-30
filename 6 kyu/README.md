# Summaries
## Challenges under level 6 kyu 

### 1: Create a phone number
  - Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number like so.
    ```python
    create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
    ```
  - The returned format must be correct in order to complete this challenge.
  - Don't forget the space after the closing parentheses!
#### Solution
  - [Create a Phone Number](./create_phone_no.py)
### 2: Who likes this?
  - You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.
  - Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:
  ``` python
  []                                -->  "no one likes this"
  ["Peter"]                         -->  "Peter likes this"
  ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
  ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
  ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
  ```
  - Note: For 4 or more names, the number in "and 2 others" simply increases.
#### Solution
- [Who is this.py](./who_is_this.py)



### 3: Count the number of Duplicates
- Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. - The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits like so:

  ```
  "abcde" -> 0 # no characters repeats more than once
  "aabbcde" -> 2 # 'a' and 'b'
  "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
  "indivisibility" -> 1 # 'i' occurs six times
  "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
  "aA11" -> 2 # 'a' and '1'
  "ABBA" -> 2 # 'A' and 'B' each occur twice
  ```
#### Solution
- [Duplicate Letter Counter](./duplicate_count.py)
