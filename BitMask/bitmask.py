'''
BitMask 알고리즘

# 특정 비트 설정
# 특정 비트 지우기
# 특정 비트 토글
# 특정 비트 확인

비트는 오른쪽에서 왼쪽으로 읽고, 0부터 시작함을 상기하자.
'''


def set_bit(x, pos):
    """
    Set the bit at 'pos' to 1.

    Args:
    x (int): The original number.
    pos (int): The position of the bit to set (0-based).

    Returns:
    int: The number with the bit at 'pos' set to 1.
    """
    return x | (1 << pos)


def clear_bit(x, pos):
    """
    Clear the bit at 'pos' to 0.

    Args:
    x (int): The original number.
    pos (int): The position of the bit to clear (0-based).

    Returns:
    int: The number with the bit at 'pos' cleared to 0.
    """
    return x & ~(1 << pos)


def toggle_bit(x, pos):
    """
    Toggle the bit at 'pos' (if it is 1, make it 0; if it is 0, make it 1).

    Args:
    x (int): The original number.
    pos (int): The position of the bit to toggle (0-based).

    Returns:
    int: The number with the bit at 'pos' toggled.
    """
    return x ^ (1 << pos)


def check_bit(x, pos):
    """
    Check if the bit at 'pos' is set to 1.

    Args:
    x (int): The original number.
    pos (int): The position of the bit to check (0-based).

    Returns:
    bool: True if the bit at 'pos' is 1, False otherwise.
    """
    return (x & (1 << pos)) != 0


# Example usage:
x = 0b1010  # binary for 10

# Set the 1st bit
x = set_bit(x, 1)  # 1010 | 0010 -> 1010 (10)
print(bin(x))  # Output: 0b1010

# Set the 0th bit
x = set_bit(x, 0)  # 1010 | 0001 -> 1011 (11)
print(bin(x))  # Output: 0b1011

# Clear the 3rd bit
x = clear_bit(x, 3)  # 1011 & 0111 -> 0011 (3)
print(bin(x))  # Output: 0b11

# Toggle the 1st bit
x = toggle_bit(x, 1)  # 0011 ^ 0010 -> 0001 (1)
print(bin(x))  # Output: 0b1

# Check if the 0th bit is set
is_set = check_bit(x, 0)  # 0001 & 0001 -> True
print(is_set)  # Output: True

# Check if the 2nd bit is set
is_set = check_bit(x, 2)  # 0001 & 0100 -> False
print(is_set)  # Output: False
