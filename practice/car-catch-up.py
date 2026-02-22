from typing import Dict, List

def main():
    x = [3,1, 2]
    y = ["c", "a", "b"]

    z = list(zip(x, y))
    print(z)

    for a in z:
        print(f"{a[0]}, {a[1]}")
    
    z.sort(key = lambda x: x[0], reverse=True)

    z2 = sorted(z, key=lambda x: x[0], reverse=True)
    for a in z:
        print(f"{a[0]}, {a[1]}")

if __name__ == "__main__":
    main()