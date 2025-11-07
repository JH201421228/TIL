import sys, math
sys.stdin = open("input.txt")
input = sys.stdin.readline


PI = math.pi


def getArea(circles):
    


    return


def solve():
    circles = list(map(float, input().split()))

    centric_length = ((circles[0] - circles[3])**2 + (circles[1] - circles[4])**2)**.5

    r1_r2_add = circles[2] + circles[5]
    r1_r2_sub = abs(circles[2] - circles[5])

    if centric_length >= r1_r2_add: 
        print(0.00)
    elif centric_length <= r1_r2_sub:
        print(PI * (min(circles[2], circles[5])**2))
    else:
        theta1 = math.acos((circles[2]**2 - circles[5]**2 + centric_length**2) / (2*circles[2]*centric_length))
        theta2 = math.acos((-circles[2]**2 + circles[5]**2 + centric_length**2) / (2*circles[5]*centric_length))

        res1 = (circles[2]**2 * theta1) - (circles[2]**2 * math.sin(2*theta1) / 2)
        res2 = (circles[5]**2 * theta2) - (circles[5]**2 * math.sin(2*theta2) / 2)

        print(res1 + res2)

    return


def main():
    solve()

    return


if __name__ == "__main__":
    main()