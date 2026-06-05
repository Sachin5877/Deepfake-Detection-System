import os

p = "D:\\deepfake_faces"

for s in os.listdir(p):
    sp = os.path.join(p, s)

    if os.path.isdir(sp):
        print(f"\n{s.upper()}")

        for c in os.listdir(sp):
            cp = os.path.join(sp, c)

            if os.path.isdir(cp):
                n = len(os.listdir(cp))
                print(f"{c}: {n}")