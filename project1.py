# Write a program that will check if is a digit and five digitslong

zip_code = input ("Enter a zip code: ").strip()
if zip_code .isdigit() and len(zip_code) == 5:
    print("Valid zip code")
else:
    print("invalid zip code")
    