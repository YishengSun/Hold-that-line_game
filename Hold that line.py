from random import choice


def creat_table(rows, columns):
    table = []

    for x in range(rows):
        row = []
        for y in range(columns):
            row.append((x, y))
            if len(row) == columns:
                table.append(row)
            else:
                pass

    return table


def multiply(v1, v2):
    return v1.x * v2.y - v2.x * v1.y


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


class Segment:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def straddle(self, another_segment):
        v1 = another_segment.point1 - self.point1
        v2 = another_segment.point2 - self.point1
        vm = self.point2 - self.point1
        if multiply(v1, vm) * multiply(v2, vm) <= 0:
            return True
        else:
            return False

    def is_cross(self, another_segment):
        if self.straddle(another_segment) and another_segment.straddle(self):
            return True
        else:
            return False


# Get all possible sets of segments
def get_possible_segments(e_nodes, a_a_nodes):
    p_segments = []
    for end in e_nodes:
        for other_node in a_a_nodes:
            p_segments.append([end, other_node])
    return p_segments


# Checks and returns all feasible segments
def get_feasible_segments(segments1, segments2):
    f_segments = []
    for new_seg in segments1:
        num = 0
        for existed_seg in segments2:
            a = Point(new_seg[0][0], new_seg[0][1])
            b = Point(new_seg[1][0], new_seg[1][1])
            c = Point(existed_seg[0][0], existed_seg[0][1])
            d = Point(existed_seg[1][0], existed_seg[1][1])
            ab = Segment(a, b)
            cd = Segment(c, d)
            if ab.is_cross(cd):
                pass
            else:
                num += 1  # Record the number of existing segments that do not intersect this segment

            if num == len(segments)-1:    # if only one of all existing segments intersects it (this one because the new
                f_segments.append(new_seg) # segment is drawn from the end of the old segment, so it must intersect at least 1)
            else:
                pass
    return f_segments


table1 = creat_table(4, 4)
all_available_nodes = []
for i in table1:
    for j in i:
        all_available_nodes.append(j)


end_nodes = []
pass_nodes = []
segments = []

while 1 == 1:

    # Input the head and tail of the segment
    head = list(map(int, list(input('Please input your start node pos(Directly input coordinates such as (0,1) enter 01): '))))
    # Input validation should be added to check the scope and availability
    tail = list(map(int, list(input('Please input your end node pos: '))))
    # Input validation should be added to check the scope and availability

    # Store end points and line segments
    t_head = tuple(head)
    t_tail = tuple(tail)
    segments.append([t_head, t_tail])

    # Move the old end node from the end nodes set to the pass nodes set, and add new end node,
    # so there are always only two end nodes
    if t_head in end_nodes:
        end_nodes.remove(t_head)
        pass_nodes.append(t_head)
        end_nodes.append(t_tail)
    else:
        end_nodes.append(t_head)
        end_nodes.append(t_tail)

    # Check if the connection passes through the intermediate node, if so, save the intermediate node
    def check_pass(head_tuple, tail_tuple, p_nodes):

        if tail_tuple[0] - head_tuple[0] == tail_tuple[1] - head_tuple[1]:
            cor_x = min(head_tuple[0], tail_tuple[0])
            cor_y = min(head_tuple[1], tail_tuple[1])
            for count in range(abs(head_tuple[1] - tail_tuple[1]) - 1):
                cor_x += 1
                cor_y += 1
                p_nodes.append((cor_x, cor_y))
        elif head_tuple[1] == tail_tuple[1]:
            cor_x = min(head_tuple[0], tail_tuple[0])
            for count in range(abs(head_tuple[0]-tail_tuple[0]) - 1):
                cor_x += 1
                p_nodes.append((cor_x, head_tuple[1]))

        elif head_tuple[0] == tail_tuple[0]:
            cor_y = min(head_tuple[1], tail_tuple[1])
            for count in range(abs(head_tuple[1]-tail_tuple[1]) - 1):
                cor_y += 1
                p_nodes.append((head_tuple[0], cor_y))

        else:
            pass

        return p_nodes

    # Check win/lose. If lose, it exits the loop. And if it's feasible to give any line, it returns to the first step
    pass_nodes = check_pass(t_head, t_tail, pass_nodes)

    for node in list(set(pass_nodes).union(set(end_nodes))):
        if node in all_available_nodes:
            all_available_nodes.remove(node)
        else:
            pass

    possible_segments = get_possible_segments(end_nodes, all_available_nodes)
    feasible_segments = get_feasible_segments(possible_segments, segments)
    # print(possible_segments)
    # print(feasible_segments)

    if len(feasible_segments) == 0:

        print("Sry, You lose!")
        break
    else:
        next_segment = choice(feasible_segments)
        segments.append(next_segment)
        pass_nodes = check_pass(next_segment[0], next_segment[1], pass_nodes)

        end_nodes.remove(next_segment[0])
        pass_nodes.append(next_segment[0])
        # print(pass_nodes)
        end_nodes.append(next_segment[1])
        for node in list(set(pass_nodes).union(set(end_nodes))):
            if node in all_available_nodes:
                all_available_nodes.remove(node)
        possible_segments = get_possible_segments(end_nodes, all_available_nodes)
        # print(possible_segments)
        feasible_segments = get_feasible_segments(possible_segments, segments)
        # print(feasible_segments)

        if len(feasible_segments) == 0:
            print('You win!')
            break
        else:
            print('I draw: ' + str(next_segment))




























