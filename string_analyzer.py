# String Analyzer Program
# Author: Divya Reddy
# Description: A program that performs multiple string operations and analyses.

def analyze_string(s):
    print("\n--- String Analysis ---")
    print(f"Original String: {s}")
    print(f"Length of String: {len(s)}")
    print(f"Uppercase: {s.upper()}")
    print(f"Lowercase: {s.lower()}")
    print(f"Title Case: {s.title()}")
    print(f"Reversed: {s[::-1]}")

    # Check if palindrome
    if s.lower() == s[::-1].lower():
        print("Palindrome: Yes ✅")
    else:
        print("Palindrome: No ❌")

    # Count vowels and consonants
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for ch in s if ch in vowels)
    consonant_count = sum(1 for ch in s if ch.isalpha() and ch not in vowels)
    print(f"Vowels: {vowel_count}")
    print(f"Consonants: {consonant_count}")

    # Count frequency of each character
    freq = {}
    for ch in s:
        if ch.isalpha():
            freq[ch.lower()] = freq.get(ch.lower(), 0) + 1
    print("\nCharacter Frequency:")
    for char, count in freq.items():
        print(f"{char}: {count}")

    # Count words
    words = s.split()
    print(f"\nTotal Words: {len(words)}")
    print(f"Words List: {words}")

    # Find longest and shortest word
    if words:
        longest = max(words, key=len)
        shortest = min(words, key=len)
        print(f"Longest Word: {longest}")
        print(f"Shortest Word: {shortest}")

if __name__ == "__main__":
    print("🔤 STRING ANALYZER 🔤")
    user_input = input("Enter a string to analyze: ").strip()
    analyze_string(user_input)
