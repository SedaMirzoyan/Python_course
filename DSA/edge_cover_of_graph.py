import math

#Calculate the Edge Cover of a Graph
def calc_edge_cover(num_vert):
    edge_cover = math.ceil(num_vert/2) 

    return edge_cover


def main():
    num_vert = 8
    print(calc_edge_cover(num_vert))


if __name__== "__main__":
    main()