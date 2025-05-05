# Each year for a human is like 7.18 years for a dog
DOG_YEARS_MULTIPLIER = 7.18  

def main():
    age_in_calendar_years = int(input("Enter an age in calendar years: ")) 
    dog_years = 7.18
    age_in_dog_years = age_in_calendar_years * dog_years
    print(f"That's {age_in_dog_years} in dog years!")


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()