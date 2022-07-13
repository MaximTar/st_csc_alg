# по данным n отрезкам необходимо найти множество точек минимального размера,
# для которого каждый из отрезков содержит хотя бы одну из точек


def points(lst):
    if lst:
        pts = []
        sorted_lst = sorted(lst, key=lambda x: x[1])
        pts.append(sorted_lst[0][1])
        for seg in sorted_lst:
            if not seg[0] <= pts[-1] <= seg[1]:
                pts.append(seg[1])
        return pts


def main():
    n = int(input())
    segments = []
    for _ in range(n):
        segments.append(list(map(int, input().split())))
    pts = points(segments)
    print(len(pts))
    print(*pts)


if __name__ == "__main__":
    main()
