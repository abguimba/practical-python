# bounce.py
#
# Exercise 1.5

def main():
    height = 100
    for bounce in range(1, 11):
        height *= 0.6
        print(f"{bounce} {str(round(height, 4))}")

if __name__ == "__main__":
    main()
